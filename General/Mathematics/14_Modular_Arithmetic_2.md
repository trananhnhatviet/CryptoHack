# **#Modular Arithmetic 2**
-   Bài này khá là hay, với thuật toán khá là đơn giản, đọc docx dưới đây
    https://stackoverflow.com/questions/2177781/how-to-calculate-modulus-of-large-numbers

-   Ví dụ 5^6 mod 9
        1 * 5 = 5 mod 9
        5 * 5 = 7 mod 9
        7 * 5 = 8 mod 9
        8 * 5 = 4 mod 9
        4 * 5 = 2 mod 9
        2 * 5 = 1 mod 9
    --> 5^6 = 1 mod 9

-    Đoạn code sẽ như sau:
```
    a = 273246787654
    p = 65537
    remainder = 1
    for i in range(1, 65537):
        x = remainder * a
        remainder = x % p
    print(remainder)

```

-   Và cờ của bài này là: ***1***
