# **#8.Inferius Prime**

![](https://i.imgur.com/wSUf0Bm.png)

-   Chall này khá giống với RSA Starter 5, chỉ decode plaintext thành bytes

-   Chall cho ta 1 file output.txt gồm:

    +   n = 742449129124467073921545687640895127535705902454369756401331
    +   e = 3
    +   ct = 39207274348578481322317340648475596807303160111338236677373


-   Từ n, ta có:
    +   p = 752708788837165590355094155871
    +   q = 986369682585281993933185289261

-   Tiếp theo ta tính phi
    +   phi = (p-1)*(q-1)

-   Tìm private key d = inverse(e,phi)

-   Plaintext = pow (ct,d,n)

-   Khi ta đã có được plaintext là 1 số nguyên lớn, ta decode nó sang byte
    +   decrypted = long_to_bytes(plaintext)

-   Decrypted chính là flag cần tìm

-   Đoạn code như sau:
```
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
p = 752708788837165590355094155871
q = 986369682585281993933185289261

phi = (p-1)*(q-1)

d = inverse (e,phi)



pt = pow(ct, d, n)
decrypted = long_to_bytes(pt).decode()
print(decrypted)

```

***Flag của bài này là: crypto{N33d_b1g_pR1m35}***