# Flipping Cookie

![](https://i.imgur.com/BPMmEye.png)

-   Chall đưa cho ta source code như sau:

```
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = ?
FLAG = ?


@chal.route('/flipping_cookie/check_admin/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


@chal.route('/flipping_cookie/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}
```
-   Trước khi đọc tiếp, tui nghĩ nên đọc cái này thì sẽ dễ hiểu hơn [Click_here](https://bernardoamc.com/cbc-bitflipping-attack/?fbclid=IwAR0zODFIiucy0LP6CUpTlF1D5JTOTWR1V3CaEOTFmU-_kW24KTLOl9LlEq4)
-   Có nghĩa là khi check_admin, nhập cookie và iv sao cho xuất hiện ``admin=True`` thì sẽ xuất hiện flag
-   Thế nhưng cookie ban đầu lại có dạng là ``admin=False;expiry=1681921755``  (1681921755 là thời gian hiện tại)
-   Làm thế nào để ta có thể chuyển về thành ``admin=True`` ???
-   Khi ta thu cookie từ hàm get_cookie(), ta sẽ thu được 1 đoạn ciphertext = iv.hex() + encrypted.hex(), ta chia ra thành 3 phần là:
    -   iv = cookie[:16] # Đây là iv ban đầu
    -   block1 = cookie[16:32] # block_data_1_after_encrypt
    -   block2 = cookie[32:]   # đoạn còn lại của cookie
-   Trước hết, ta cần ôn lại cách mã hóa và giải mã của CBC
    ![](https://i.imgur.com/iqBozyL.png)

-   Cho ``origin = b'admin=False;expi'``
-   Ta thấy rằng, đoạn ``admin=False;expi`` chắc chắn sẽ được Xor với iv và nó chính là block1 --> block1 có dạng: ``block1 = iv ^ origin'``
-   Tiếp theo, ta có 1 đoạn 16 byte ``target_to_get_flag = b'admin=True_yeah\x01'`` (Mình thêm 'yeah' chỉ để vui, và \x01 là PKCS#7 Padding)
-   Ta có tính chất của Xor như sau: ``a ^ b ^ c ^ a ^ b = c``
-   Suy ra, để đạt được target thì ta cần làm các bước như sau:
    -   Ta cần 1 biến xor 3 phần iv, block1 và target_to_get_flag: ``send_iv = xor(xor(origin, target_to_get_flag),(iv))``
    -   Thực ra hàm check_admin cũng chỉ là hàm giải mã của CBC, và khi giải mã, ta sẽ gửi block1 và send_iv vào hàm check_admin: ``check_admin(block1, send_iv)``
    -   Khi giải mã, IV sẽ xor với đầu ra của block cipher decrytion để ra plaintext, tức là block1 sẽ tiếp tục xor với send_iv --> ``output = target_to_get_flag ^ iv ^ origin ^ iv ^ origin = target_to_get_flag = b'admin=True_yeah\x01'``
-   Khi đạt được target, ta sẽ thu được cờ
    ![](https://i.imgur.com/ncSFqDO.png)
-   Đoạn code minh họa quá trình giải mã như sau:
```
from Crypto.Cipher import AES
import os
from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad


KEY = b'this_is_a_keycbc' # KEY 16 byte

# a ^ b
def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))


# Hàm check_admin này giống hệt trong challenge đưa ra
def check_admin(cookie, iv):
    
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(cookie)
    unpadded = unpad(decrypted, 16)
    
    # Nếu ra admin=True thì là đúng
    if b"admin=True" in unpadded:
        print(unpadded)
    else:
        print('false')


# Hàm get_cookie này giống hệt trong challenge đưa ra
def get_cookie():
    expires_at ='1681921755' #Đây là (datetime.today() + timedelta(days=1)).strftime("%s") tại thời điểm hiện tại
    data = f"admin=False;expiry={expires_at}".encode()
    print(data)
    iv = os.urandom(16)
    padded = pad(data, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}

# Nhận giá trị cho cookie
cookie = get_cookie()
cookie = cookie['cookie']
cookie = bytes.fromhex(cookie) # Chuyển sang byte để iv là 1 chuỗi byte

iv = cookie[:16] # Đây là iv ban đầu
block1 = cookie[16:32] # block_data_1_after_encrypt
block2 = cookie[32:]   # block_data_2_after_encrypt


origin = b'admin=False;expi' # Lấy 16 byte
target_to_get_flag = b'admin=True_yeah\x01' # PKCS#7 Padding thêm để đủ 16 byte (Mình thích thì mình thêm yeah)

# send_iv = origin ^ iv ^ target_to_get_flag
send_iv = xor(xor(origin, target_to_get_flag),(iv))

# Check Admin
check_admin(block1, send_iv)
```
-   Đọc đoạn code trên, bạn sẽ hiểu được các bước mình đã hướng dẫn ở trên
-   Đoạn code để lấy flag sẽ như sau:
```
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import*

# a ^ b
def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

# Hàm lấy giá trị cookie từ server
def get_cookie():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    
    get_cookie_value_on_server = requests.get(url)
    json_cookie = get_cookie_value_on_server.json()
    return bytes.fromhex(json_cookie["cookie"])


def check_admin(cookie, iv):
    # Kết hợp các url lại với nhau
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"
    url += cookie.hex()
    url += "/"
    url += iv.hex()
    url += "/"
    
    # Lấy flag thui nèooooo
    get_flag = requests.get(url)
    flag = get_flag.json()
    print(flag)

cookie = get_cookie()

origin = b'admin=False;expi'

# Vì trong server có đoạn code này if b"admin=True" in unpadded.split(b";"): nên phải để target_to_get_flag thế
target_to_get_flag = b'admin=True;\x05\x05\x05\x05\x05' 

iv = cookie[:16] # Đây là iv ban đầu
block1 = cookie[16:32] # block_data_1_after_encrypt
block2 = cookie[32:]   # Các đoạn còn lại

# send_iv = origin ^ iv ^ target_to_get_flag
send_iv = xor(xor(origin, target_to_get_flag), iv)

# Check Admin
check_admin(block1, send_iv)
```
***Flag của chall này là: crypto{4u7h3n71c4710n_15_3553n714l}***