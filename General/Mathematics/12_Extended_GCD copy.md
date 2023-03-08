# **#Extended GCD**
-   Trước hết, ta phải hiểu được thuật toán của bài này
    http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html

-   Ví dụ:
    a = 6, b = 10
    10 = 1(6)+4
    6 = 1(4) + 2
    4 = 2(2) + 0 -->gcd(6,10) = 2

--> 2 = 6 - 1(4) = 6 - 1( 10 - 1(6) ) = 2(6) - 1(10)

-   Đoạn code sẽ như sau:
```
    def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, remainder = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,remainder, u,v, m,n
        gcd = b
        return gcd, x, y

    print (egcd(26513,32321))
```



-   Và cờ của bài này là số bé hơn: ***-8404***
