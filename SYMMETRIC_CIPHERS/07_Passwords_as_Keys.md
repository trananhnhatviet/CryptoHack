# Passwords as Keys
![](https://i.imgur.com/j33sYZk.png)

-   Chall này cũng là dạng ECB, thế nhưng ta lại không biết Key là gì, chỉ biết Key là kết quả của băm MD5 của 1 từ trong file /usr/share/dict/words
-    Giờ để thu được các từ này vào 1 file thì ta vào đường link này [link](https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words)
-   Xong giờ ta copy và lưu vào 1 file password.txt như thế này (nhớ là lưu cùng với folder của solve.py)
![](https://i.imgur.com/gPv6xVp.png)

-   Như bài trước, ta cần request tới địa chỉ /encrypt_flag/ để thu được ciphertext

```
url = 'http://aes.cryptohack.org/passwords_as_keys/'

r = requests.get(f'{url}encrypt_flag/')
first_request = r.json()
print(first_request)
ciphertext = first_request['ciphertext']
```

-   Giờ ta brute force hết cái file password.txt đó từng từ cho tới khi thu được flag

```
with open("password.txt") as f:
    words = [w.strip() for w in f.readlines()]
    
for i in words:
    keyword = i
    KEY = hashlib.md5(keyword.encode()).digest().hex()
    s= decrypt(ciphertext,KEY)
    a=(bytes.fromhex(s))
    if b'crypto' in a:
        print(a)
        break
```

-   Đoạn code full sẽ như sau:
```
from Crypto.Util.number import*
from Crypto.Cipher import AES
import hashlib
import requests
import random

# Hàm decrypt lấy ở trang web đó lunnn
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return decrypted.hex()

url = 'http://aes.cryptohack.org/passwords_as_keys/'

r = requests.get(f'{url}encrypt_flag/')
first_request = r.json()
print(first_request)
ciphertext = first_request['ciphertext']

with open("password.txt") as f:
    words = [w.strip() for w in f.readlines()]
    
for i in words:
    keyword = i
    KEY = hashlib.md5(keyword.encode()).digest().hex()
    s= decrypt(ciphertext,KEY)
    a=(bytes.fromhex(s))
    if b'crypto' in a:
        print(a)
        print(keyword)
        break
```
***Flag chall này là: crypto{k3y5__r__n07__p455w0rdz?}***