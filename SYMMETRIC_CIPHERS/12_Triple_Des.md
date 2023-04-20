# Triple Des

![](https://i.imgur.com/Y2B57CL.png)

-   Source code của chall này như sau:
```
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad


IV = os.urandom(8)
FLAG = ?


def xor(a, b):
    # xor 2 bytestrings, repeating the 2nd one if necessary
    return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))



@chal.route('/triple_des/encrypt/<key>/<plaintext>/')
def encrypt(key, plaintext):
    try:
        key = bytes.fromhex(key)
        plaintext = bytes.fromhex(plaintext)
        plaintext = xor(plaintext, IV)

        cipher = DES3.new(key, DES3.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        ciphertext = xor(ciphertext, IV)

        return {"ciphertext": ciphertext.hex()}

    except ValueError as e:
        return {"error": str(e)}


@chal.route('/triple_des/encrypt_flag/<key>/')
def encrypt_flag(key):
    return encrypt(key, pad(FLAG.encode(), 8).hex())
```
-   Chall này là mã hóa loại TripleDes, ta thấy trên server không có hàm decrypt, ta khó có thể tìm ra flag được, thế nhưng TripleDes lại có 1 điểm yếu là [Weak_Key](https://en.wikipedia.org/wiki/Weak_key). Weak key là những khóa mà khi ta mã hóa 2 lần, ta sẽ thu được plaintext ban đầu, tức là ``Encrypt(Encrypt(Plaintext)) = Plaintext``
-   Gồm các Weak Key như sau:
    ![](https://i.imgur.com/McKJpme.png)

-   Chall này, ta cần sử dụng các Weak Key để có thể tìm được Flag
-   Chọn 3 Weak Key để làm, mình chọn 3 khóa là ``b'\x00'*8``, ``b'\xff'*8``, ``b'\x01'*8 ``
-   Sơ đồ cách làm như sau:
    ![](https://i.imgur.com/ZPj2GCN.png)
-   Đoạn code minh họa cho sơ đồ trên:
```
from Crypto.Cipher import DES3,DES
import os
from Crypto.Util.Padding import pad,unpad


IV = os.urandom(8)
FLAG = b'Flag{This_is_flag}'


def xor(a, b):
    # xor 2 bytestrings, repeating the 2nd one if necessary
    return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))

def decrypt_des(key, ciphertext):
    key = bytes.fromhex(key)
    ciphertext = bytes.fromhex(ciphertext)
    cipher = DES.new(key,DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.hex()

def encrypt_des(key, plaintext):
    key = bytes.fromhex(key)
    plaintext = bytes.fromhex(plaintext)
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()


key_1 = b'\x00'*8 
key_2 = b'\xff'*8 
key_3 = b'\xfe'*8
key_1 = key_1.hex()
key_2 = key_2.hex()
key_3 = key_3.hex()
FLAG_pad = pad(FLAG,8)
FLAG_after_xor = xor(FLAG_pad,IV) 

# First block 3DES
flag_first = (encrypt_des(key_1,(FLAG_after_xor).hex()))
flag_second = (decrypt_des(key_2,flag_first))
flag_third = (encrypt_des(key_3,flag_second))

#Second block 3DES
flag_fourth = (encrypt_des(key_1,flag_third))
flag_fifth = (decrypt_des(key_2,flag_fourth))
flag_sixth = (encrypt_des(key_3,flag_fifth))
print(unpad((xor(bytes.fromhex(flag_sixth),IV)),8).decode())
```

-   Đoạn code của chall này là:
```
import requests

def encrypt(key, plain):
    url = "http://aes.cryptohack.org/triple_des/encrypt/"
    url += key
    url += "/"
    url += plain.hex()
    url += "/"
    r = requests.get(url).json()
    return bytes.fromhex(r["ciphertext"])

def encrypt_flag(key):
    url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    r = requests.get(url + key + '/').json()
    return bytes.fromhex(r["ciphertext"])
key1 = b'\x00'*8
key2 = b'\xff'*8
key3 = b'\x01'*8
key = key1.hex() + key2.hex() + key3.hex()

enc_flag = encrypt_flag(key)
ciphertext = encrypt(key, enc_flag)
print(ciphertext)
```
***Flag chall này là: crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}***