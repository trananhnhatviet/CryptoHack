# **#ASCII**

![](https://i.imgur.com/AxQJere.png)


-    Mô tả: Mục đích chall này là giúp chúng ta hiểu về bảng Ascii, hiểu các mã cơ bản như decimal, hexa, binary, octal sang kí tự Ascii sẽ như thế nào và ngược lại

![](https://i.imgur.com/iaUvuvz.png)


-    Ta thấy đề cho 1 list các số nguyên như sau:
    [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

-   Ta cần sử dụng các hàm:
    +   chr(): chuyển từ decimal sang ascii
    +   ord(): chuyển từ ascii sang decimal
    
-    Ta nhận thấy đây là các mã decimal, qua đó ta phải dùng chr() để có thể chuyển về các kí tự
    
-    Đoạn code sẽ như sau:
```
    lst=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    flag=""
    for i in lst:
        flag =flag+chr(i)
    print(flag)
```
-    Và cờ của bài này là: ***crypto{ASCII_pr1nt4bl3}***