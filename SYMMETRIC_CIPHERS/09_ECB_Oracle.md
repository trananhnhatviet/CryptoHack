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
-   Bạn có thể đọc link sau đây để tham khảo [clickhere](https://crypto.stackexchange.com/questions/42891/chosen-plaintext-attack-on-aes-in-ecb-mode)
-   Đây chính là cách tấn công ECB Oracle, một dạng tấn công bruteforce
-   Các block giống nhau thì sẽ thu được về các đoạn mã hóa giống nhau
-   Ví dụ ta có 1 bài encrypt ECB cơ bản như sau:
```
from Crypto.Cipher import AES

block_1 = '00000000000000000000000000000063' #hexacdecimal
block_2 = '00000000000000000000000000000063' #hexadecimal
data = bytes.fromhex(block_1) + bytes.fromhex(block_2)
key = b'1234567812345678'


def encrypt_data(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypt = cipher.encrypt(plaintext)
    return encrypt

encrypt_data_block1 = (encrypt_data(data)[:16])
encrypt_data_block2 = (encrypt_data(data)[16:])

print(encrypt_data_block1)
print(encrypt_data_block2)


#Output:
#   b"\xb6#=E\r\xe5\x80\x84\xed@}!'\x9d\x97\xeb"
#   b"\xb6#=E\r\xe5\x80\x84\xed@}!'\x9d\x97\xeb"
```
-   Ta thấy rất rõ ràng, 2 block sẽ giống hệt nhau, mà chall này, đoạn plaintext mình nhập vào sẽ được thêm flag rồi mã hóa cũng 1 lượt
-   Ta có ý tưởng là như sau:
    -   Ban đầu, ta cần tạo 1 đoạn hexa 31 byte --> 1 byte còn lại sẽ là 1 kí tự của flag
    -   Ta sẽ gửi lên server 2 đoạn hexa '000000000000000000000000000000``xx``' (16 byte) cùng với 1 đoạn hexa '00'x32 và '000000000000000000000000000000' (15 byte), ta sẽ bruteforce ``xx`` sao cho thu được 2 block mã hóa giống nhau
    -   Ta đoán được flag sẽ có ký tự 'c' đầu tiên nên ta gửi đoạn hexa 1 là '00000000000000000000000000000063' và nối thêm 2 đoạn hexa 
    ![](https://i.imgur.com/9qqjBzz.png)
    -   Sau đó, ta thu được ký tự 'c'
    -   Tiếp theo, ta gửi 1 đoạn hexa '000000000000000000000000000063`xx`'(16 byte) cùng '00'x32 và 1 đoạn '0000000000000000000000000000' (14 byte) lên server, ta cần phải giảm byte vì phải để chỗ cho các ký tự của flag nhập vào đoạn hexa cuối
    -   Khi flag có độ dài là 16, ta cần bỏ bớt 1 ký tự đầu của flag đi để có thể thành 16 byte nhaaa
    -   Bruteforce cho tới khi thu được cờ thuiiii
-   Đoạn code sẽ như sau:
```
import requests
from string import printable


def encrypt(plaintext):
    url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
    url = url + plaintext
    url = url + '/'
    r = requests.get(url)
    js = r.json()
    output = js['ciphertext']
    return output


flag = 'crypto{'
flag_byte = b'crypto{'
while flag[len(flag)-1] != '}':
    if len(flag)>=16:
            flag_byte = flag_byte[1:]
    for i in printable:
        block_hexa = ""
        for j in range(16-len(flag_byte)-1):
            block_hexa = block_hexa + '00'
        i_byte = bytes(i,'utf-8')
        flag_to_hex = flag_byte.hex()
        plaintext = block_hexa + flag_to_hex+(i_byte).hex()+'00'*(31-len(flag))
        print(plaintext)
        ciphertext = encrypt(plaintext)
        if ciphertext[:32] == ciphertext[64:64+32]:
            flag = flag + i
            flag_byte = flag_byte + bytes(i,'utf-8')
            print(flag)
            break
print(flag)
```

***Flag của chall này là: crypto{p3n6u1n5_h473_3cb}***