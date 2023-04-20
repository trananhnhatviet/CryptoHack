# Modes of Operation Starter

![](https://i.imgur.com/qRcKZXb.png)

-   Chúng ta bắt đầu với các loại mã hõa AES, nếu bạn chưa biết gì về ECB thì hãy dừng lại và đọc cái này đi [clickhere](https://github.com/trananhnhatviet/AES_cipher/blob/main/Block_cipher_modes_of_operation.md) hoặc là lên ytb xem đi nhaaa

-   Chall này giúp ta biết các mã hóa bằng ECB là như thế nào và cách dùng thư viện request

-   Ta có 1 source code như sau:
```
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```
-   Khi ta request tới /encrypt_flag/ thì ta thu được 1 json chứa ciphertext như sau:
![](https://i.imgur.com/fTYFqnd.png)

-   Giờ ta chỉ cần request tới /decrypt/ciphertext/ là sẽ thu được plaintext dưới dạng hexadecimal rồi ta chuyển về byte thì sẽ thu được flag của chall này
-   Mình hiện tại chưa quen dùng request nên mình có tham khảo wu của anh [Thắng](https://hackmd.io/@Thangcoithongminh/rkungRrUo) nha

```
import requests

url = "http://aes.cryptohack.org/block_cipher_starter"

# Kết nối lần 1 với http://aes.cryptohack.org/block_cipher_starter/encrypt_flag
first_request = requests.get(f"{url}/encrypt_flag")
# Nhận giá trị của json
data_ciphertext = first_request.json()
print(data_ciphertext)
ciphertext = data_ciphertext['ciphertext']
print(ciphertext)
#Ciphertext là: 11bbdda0a15bd72de52f8b2af8bacd9c806bd93bd6ba80e556b291ddec068455

# Kết nối lần 1 với http://aes.cryptohack.org/block_cipher_starter/decrypt/11bbdda0a15bd72de52f8b2af8bacd9c806bd93bd6ba80e556b291ddec068455
second_request = requests.get(f'{url}/decrypt/{ciphertext}/')
# Nhận giá trị json
data_plaintext_hex = second_request.json()
print(data_plaintext_hex)
plaintext = data_plaintext_hex['plaintext']
print(plaintext)
# Chuyển về bytes
flag = bytes.fromhex(plaintext)
print(flag)

```
***Flag của chall này là: crypto{bl0ck_c1ph3r5_4r3_f457_!}***