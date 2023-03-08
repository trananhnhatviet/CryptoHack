# **#RSA Starter 5**

![](https://i.imgur.com/ZG3bRSY.png)

-   Chall này bắt ta phải dùng N và e decrypt ciphertext:

    +   ciphertext = 77578995801157823671636298847186723593814843845525223303932

-   Trước hết, ta cần tìm p và q

    +   p = 857504083339712752489993810777
    +   q = 1029224947942998075080348647219

-   Tính phi của N

    +   phi = (p-1)*(q-1)

-   Khi đó, private key d sẽ bằng inverse(e,phi) hoặc là bằng pow(e,-1,phi)

    +   d = inverse(e, phi)


-   Chú ý: khi dùng hàm inverse, ta phải thêm thư viện Crypto.Util.number

-   Plaintext sẽ bằng module của ciphertext^pivate_ket mod N

    +   plaintext = pow(ciphertext,d,N)

-   Code sẽ như sau:
```
from Crypto.Util.number import long_to_bytes

N = 882564595536224140639625987659416029426239230804614613279163

e = 65537

ciphertexet = 77578995801157823671636298847186723593814843845525223303932

q = 857504083339712752489993810777

p = 1029224947942998075080348647219

phi=(p-1)*(q-1)

d=pow(e,-1,phi)

plaintext = pow(ciphertexet, d, N)

print(plaintext)
```

***Flag bài này là : 13371337***