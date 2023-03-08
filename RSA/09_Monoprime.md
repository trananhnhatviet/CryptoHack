# **#9.Monoprime**

![](https://i.imgur.com/0ImmSPr.png)

-   Chall này cho ta hiểu vì sao phải dùng 2 số nguyên tố p và q trong mật mã RSA

-   Nếu bạn giỏi tiếng anh thì click vào link sau:
    +   https://crypto.stackexchange.com/questions/5170/why-do-we-need-in-rsa-the-modulus-to-be-product-of-2-primes
-   Còn nếu không thì đây là cách hiểu của mình:
    +   RSA cần 2 số nguyên tố p và q vì chỉ có chúng thì ta mới tìm được private key
    +   Ngoài ra, nếu không có 2 số này, nó sẽ mất đi các thuộc tính bảo mật vốn có của RSA
    +   Thực chất, nếu có nhiều hơn 2 factors, thì vẫn có thể dùng RSA được, nhưng hầu hết chả ai dùng biến thể này cả

-   Chall này mình sẽ không giải thích nhiều về code vì chả có mã RSA nào mà ko dùng p và q cả, nên mình chỉ up code lên để up level thui :v:

-   Đoạn code như sau:
```
from Crypto.Util.number import long_to_bytes,inverse

N = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  

e = 65537

ciphertext = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942  

q = 857504083339712752489993810777

p = 1029224947942998075080348647219


d=inverse(e,N-1)

plaintext = pow(ciphertext, d, N)

print(long_to_bytes(plaintext))
```

***Flag của bài này là: crypto{0n3_pr1m3_41n7_pr1m3_l0l}***