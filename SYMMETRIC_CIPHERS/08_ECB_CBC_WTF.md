# ECB CBC WTF
![](https://i.imgur.com/tqDd3TE.png)

-    Chall này cho ta biết thêm 1 loại mã hóa mới, Cipher Block Chainning (CBC)
-   Source của chall này là:
```
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```
-   AES.CBC sẽ như sau:
![](https://i.imgur.com/o17XY3F.png)
-    Ta thấy ban đầu, flag sẽ được mã hóa loại CBC thế nhưng khi giải mã lại là ECB
-   Khi ta request tới /encrypt_flag/ thì ta sẽ thu được 1 đoạn hexadecimal gồm (iv) và (encrypted)
-   Đoạn đó có độ dài là 48 bytes --> Chia thành 3 đoạn là IV, encrypt_cbc_block_flag_1, encrypt_cbc_block_flag_2
![](https://i.imgur.com/e4EOJTc.png)
-   Khi ta request tới /decrypt/ciphertext thì server chỉ decrypt theo AES.ECB và ta cũng thu được 1 đoạn có độ dài là 48 bytes --> Chia thành 3 đoạn là decrypt_ecb_iv, decrypt_ecb_block_flag_1, decrypt_ecb_block_flag_2
    ![](https://i.imgur.com/EvlWpbs.png)
-   Đây là giải mã theo kiểu ECB, thế nhưng để tìm được flag thì cần giải mã theo kiểu CBC, nhưng server lỏ nên chỉ có ECB, thế nên giờ mình phải tự giải
-   Cách làm sẽ như thế này
![](https://i.imgur.com/ginj3fY.png)
-    Ta cần chia ra các đoạn và làm theo sơ đồ trên
-   Đoạn code sẽ như sau:
```
import requests
from pwn import *
from hashlib import md5
from Crypto.Cipher import AES

url = 'https://aes.cryptohack.org/ecbcbcwtf/'
first_request = requests.get(f"{url}/encrypt_flag")
flag = b''

# Nhận giá trị của json
data_ciphertext = first_request.json()
ciphertext = data_ciphertext['ciphertext']
ct = bytes.fromhex(ciphertext)
print(ct, len(ct))

second_request = requests.get(f'{url}decrypt/{ciphertext}/')
data_2 = second_request.json()
plaintext = data_2['plaintext']
pt = bytes.fromhex(plaintext)
print(pt, len(pt))
print('')

for i in range(0,len(ciphertext),16):
    print(ct[i:i+16],"      ",pt[i+16:i+32])
    flag += xor(ct[i:i+16],pt[i+16:i+32])
    print(flag)
    print('')

```
***Flag chall này là: crypto{3cb_5uck5_4v01d_17_!!!!!}***