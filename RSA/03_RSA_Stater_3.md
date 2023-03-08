# **#RSA Starter 3**

![](https://i.imgur.com/MstoZii.png)

-   Chall này sẽ cho ta biết và hiểu được cách tính φ(n)

-   Ví dụ n = 40



-   Để tính φ(40):
    +   Ta phải phân tích 20 thành các số nguyên tố và được (2x2x2x5) = (2^3 x 5^1)
    +   Ta có công thức φ(20) = 2^(3-1) x (2-1) x 5^(1-1) x (5-1)  =  2^2 x (2-1) x 5^0 x (5-1) = 16 

-   Chall cho ta biết p = 857504083339712752489993810777, q  =1029224947942998075080348647219 --> φ(n) = (p-1)*(q-1)
-   Code của bài này là 
```
    p = 857504083339712752489993810777  
    q = 1029224947942998075080348647219
    print((p-1)*(q-1))
```

***Flag bài này là : 882564595536224140639625987657529300394956519977044270821168***