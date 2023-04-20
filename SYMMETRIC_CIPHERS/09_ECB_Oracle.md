# ECB Oracle

![](https://i.imgur.com/yKJCDGG.png)

-   Chall cho ta 1 source code như sau:
```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


KEY = ?
FLAG = ?


@chal.route('/ecb_oracle/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}

```

-   Ta thấy Chall này chỉ nhận Plaintext, sau đó, plaintext sẽ cộng với Flag của chall rùi padding thêm byte, sau đó mã hóa theo dạng ECB

-   Chall này cho ta thấy được ECB là 1 loại mã hóa có bảo mật kém, dựa vào điểm yếu này, Hacker sẽ tấn công và sẽ có được thông tin cần bảo mật
-   Ví dụ ta có 1 bài encrypt ECB cơ bản như sau:
```
import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from binascii  import*
key = b'1122334455667788'            # Đây là key (phải là 16 ký tự nếu là AES 128) 
# hello_world_baby và hello_world_haha đã thành 1 block và từ _a trở đi sẽ thuộc block 2
data_1 = 'hello_world_baby_a' # Đây là dữ liệu 1 cần mã hóa
data_2 = 'hello_world_haha_a' # Đây là dữ liệu 2 cần mã hóa

def encrypt(raw): 
    raw = pad(raw.encode(),16) # Thêm các byte không có giá trị để đảm bảo độ dài là bội số của 16 
    print('raw after pad:', raw)   
    cipher = AES.new(key, AES.MODE_ECB)    
    return (cipher.encrypt(raw)).hex()

def decrypt(enc):
    enc = unhexlify(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    print('cipher:', cipher.decrypt(enc))
    return unpad(cipher.decrypt(enc),16) # Bỏ bớt các byte không có giá trị

encrypted = encrypt(data_1)
print('encrypted ECB Hexa:',encrypted)
print('')
encrypted = encrypt(data_2)
print('encrypted ECB Hexa:',encrypted)

# raw after pad: b'hello_world_baby_a\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
# encrypted ECB Hexa: b099b3742f1ac1d6ea1aab28aecd20a5(fad79d4599da81b1c2f478d7fe60bfa6)

# raw after pad: b'hello_world_baba_a\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
# encrypted ECB Hexa: 8f44c2423d5bc8f88d4f95bd122c0f0e(fad79d4599da81b1c2f478d7fe60bfa6)

```
-   Ta thấy rằng, khi mã hóa ECB 1 block plaintext giống nhau, thì ta sẽ thu được các block ciphertext giống nhau
-   Và bây giờ, ta cần phải nhập plaintext sao cho đủ 32 byte
-   Khi ta nhập plaintext dưới dạng hex ``0000000000000000000000000000006300000000000000000000000000000000000000000000000000000000000000`` ('c' = 63 (hexadecimal)), thì server sẽ gửi về 1 đoạn hexa và khi ta chuyển về byte, ta được đoạn như sau:
``
b'\xd7\x8e\x8b\xfc\x95\x1dFx\xfa\xa1\t[}\xf4\xd2\n\x0bfa!\xa8\xf3w\xae)\xfex\xabE\xbe\x96]\xd7\x8e\x8b\xfc\x95\x1dFx\xfa\xa1\t[}\xf4\xd2\ni\xf1\xa2D\xdc\x13\xfd\x02\xcdX\xca#\xae\xffq\x88u\xd1Tu\xb8b\x18\xa76HO\x97\x93k\n\xcd'
``
-   Ta thấy có 2 đoạn giống nhau đều là ``\xd7\x8e\x8b\xfc\x95\x1dFx\xfa\xa1\t[}\xf4\xd2\n`` --> Ký tự 'c' thuộc Flag cần tìm
-   Tiếp tục như thế cho tới khi bruteforce hết flag
-   Đoạn code sẽ như sau:
```
import requests

url = 'http://aes.cryptohack.org/ecb_oracle/'


flag = 'crypto{'

char_add = ''

# Đây là đoạn crypto{
load_1 = '00000000000000000063727970746f7b'

for i in range(18):
    load_1 = load_1[2:] + char_add
    for j in range(33,128):
        load = load_1 + bytes([j]).hex() + '00'*(24-i)
        print(load)
        r = requests.get(f'{url}encrypt/{load}')
        data = r.json()
        ciphertext = data['ciphertext']
        ct = bytes.fromhex(ciphertext)
        if ct[:16] == ct[32:48]:
            flag += chr(j)
            char_add = bytes([(j)]).hex()
            print(flag)
            break
```

***Flag của chall này là: crypto{p3n6u1n5_h473_3cb}***