# **#RSA Starter 1**

![](https://i.imgur.com/2LjcH4j.png)



-   Mô tả: Chall này giúp ta tìm số dư của 2 số lớn

-   Đề có cho chúng ta lý thuyết:
    +   Khi muốn chia lấy dư của 1 số mũ với 1 số tự nhiên (a mũ x mod b), ta dùng hàm pow(a,x,b) thì sẽ tìm được số dư

    +   Ví dụ 2 mũ 10 chia dư cho 17, ta dùng pow(2,10,17) thì sẽ được kết quả là 4

-   Code của bài này là 
```
    print(pow(101,17,22663))
```

***Flag bài này là : 19906***