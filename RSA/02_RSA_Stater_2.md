# **#RSA Starter 1**

![](https://i.imgur.com/pGq4f7w.png)



-   Đề có cho chúng ta lý thuyết:
    +   Mã hóa RSA là phép lũy thừa theo Module của 1 số với mũ là e và module N, tức là phép dư của (x mũ e) với N và N là tích của 2 số p và q
    +   Và e thường là 65537

-   Chall cho ta biết p = 17, q = 23, e = 65537, và số cần mã hóa là 12

-   Code của bài này là 
```
    print(pow(12,65537,17*23))
```

***Flag bài này là : 301***