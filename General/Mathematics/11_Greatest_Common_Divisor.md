# **#Greatest Common Divisor**
-   Trước hết, ta phải biết thuật toán chia lấy dư Euclid
    +   Cho 2 số nguyên a và b (a>b)
    +   Đặt 1 biến remainder = a % b
    +   Và ta dùng 1 While để lặp

-   Đoạn code sau đây sẽ giúp bạn hiểu hơn:
```
    def gcda(a,b):
        remainder=a%b
        while remainder>0:
            a=b
            b=remainder
            remainder=a%b
        return b

    a = int(66528)
    b = int(52920)
    print(gcda(a,b))  

```

-   Và cờ của bài này là: ***1512***
