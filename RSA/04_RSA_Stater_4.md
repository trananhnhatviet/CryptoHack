# **#RSA Starter 4**

![](https://i.imgur.com/HtByPRO.png)

-   Chall này sẽ giúp ta hiểu về hàm Inverse, ngoài ra còn biết tìm private key

-   Inverse thực là nghịch đảo của module

-   Module như bình thường tính bằng hàm pow(a,b,c) (tức là a^b mod c), còn khi mình dùng inverse(a,b), tức là pow(a,-1,b)

-   Khi đó, private key d sẽ bằng inverse(e,phi) hoặc là bằng pow(e,-1,phi)

-   Chú ý: khi dùng hàm inverse, ta phải thêm thư viện Crypto.Util.number

-   Code sẽ như sau:
```
from Crypto.Util.number import inverse

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

e=65537

phi = (p-1)*(q-1)

d=inverse(e,phi)

print(pow(e,-1,phi))

print(d)
```

***Flag bài này là : 121832886702415731577073962957377780195510499965398469843281***