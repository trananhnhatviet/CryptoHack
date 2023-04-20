# Lazy CBC

![](https://i.imgur.com/IiLzjLr.png)

-   Chall đưa ta source code như sau:
```
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/lazy_cbc/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    encrypted = cipher.encrypt(plaintext)

    return {"ciphertext": encrypted.hex()}


@chal.route('/lazy_cbc/get_flag/<key>/')
def get_flag(key):
    key = bytes.fromhex(key)

    if key == KEY:
        return {"plaintext": FLAG.encode().hex()}
    else:
        return {"error": "invalid key"}


@chal.route('/lazy_cbc/receive/<ciphertext>/')
def receive(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    if len(ciphertext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    decrypted = cipher.decrypt(ciphertext)

    try:
        decrypted.decode() # ensure plaintext is valid ascii
    except UnicodeDecodeError:
        return {"error": "Invalid plaintext: " + decrypted.hex()}

    return {"success": "Your message has been received"}
```

-   Chall này cho ta biết được tầm quan trọng của IV trong AES.mode nói chung và CBC nói riêng
-   Ta thấy, khi mã hóa và giải mã, thì IV = KEY, và khi ta tìm được KEY, ta sẽ thu được Valid Plaintext.
-   Đầu ra của hàm receive() là 1 Invalid Plaintext, có nghĩa là 1 bản rõ chưa chuẩn xác
-   Thế làm thế nào để tìm được KEY trong chall này ???
-   Trước hết, ta cần xem lại quá trình giải mã của CBC

    ![](https://i.imgur.com/o8GhdH0.png)

-   Bây giờ, ta chọn 1 ciphertext là đoạn null 32 byte (2 block): ``ciphertext = b'\x00' * 32``
-   Sau khi cho qua hàm receive(ciphertext), ta sẽ thu được 2 block inva_plain như sơ đồ sau đây:

    ![](https://i.imgur.com/h14ZAyo.png)
-   Ta thấy ``inva_plain_block_1 = same_value ⊕ KEY`` và ``inva_plain_block_2 = same_value ⊕ b'\x00'*16 = same_value``
-   Ta lấy 2 inva_plain_block Xor với nhau sẽ được: ``inva_plain_block_1 ⊕ inva_plain_block_2 = same_value ⊕ KEY ⊕ same_value = KEY`` --> Thu được KEY cần tìm
-   Ta gửi KEY đó lên server và lấy Valid Plaintext thuiiii :vvvv

-   Đoạn code để lấy Flag như sau:
```
import requests
from Crypto.Util.number import*


# a ⊕ b
def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))


# Kết nối với server để gửi key lấy Valid Plaintext
def get_flag(key):
    url = 'https://aes.cryptohack.org/lazy_cbc/get_flag/'
    url = url  + key
    url = url + '/'
    get_flag_requests = requests.get(url)
    flag = get_flag_requests.json()
    flag = flag['plaintext']
    return bytes.fromhex(flag).decode()



# Kết nối với server để gửi ciphertext, lấy Invalid Plaintext
def decrypt(ciphertext):
    url = "http://aes.cryptohack.org/lazy_cbc/receive/"
    url += ciphertext.hex()
    url += "/"
    plain_requests = requests.get(url)
    plain_receive = plain_requests.json()
    plain_receive = plain_receive["error"]
    return plain_receive

# Lấy ciphertext là đoạn 32 byte (2 block ciphertext)
ciphertext = b'\x00' * 32

# Lấy Invalid Plaintext và chuyển về dạng byte
invalid_plaintext = decrypt(ciphertext)
invalid_plaintext = invalid_plaintext.replace('Invalid plaintext: ','')
print("Invalid Plaintext: ",invalid_plaintext)
invalid_plaintext = bytes.fromhex(invalid_plaintext)

# Chia 2 block Invalid Plaintext
inva_plain_block_1 = invalid_plaintext[:16]
inva_plain_block_2 = invalid_plaintext[16:]
print("Block_1:",inva_plain_block_1.hex(),"       Block_2:",inva_plain_block_2.hex(),'\n')

# Xor để thu được Key của chall
Key = xor(inva_plain_block_1,inva_plain_block_2)

print("Flag:",get_flag(Key.hex()))
```
***Flag của chall này là: crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}***