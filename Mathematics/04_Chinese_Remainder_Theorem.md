# **Chinese Remainder Theorem**

![](https://i.imgur.com/VfWL9Y2.png)


-   Chall này cho ta biết được Định lý số dư Trung Quốc (hay còn gọi là Thặng dư Trung Hoa) là gì và mục đích của nó là gì
-   Thặng dư Trung Hoa (Chinese Remainder Theorem) là một phương pháp để tìm nghiệm của một hệ phương trình đồng dư có dạng:

    +   x ≡ a1 (mod m1)
    +   x ≡ a2 (mod m2)
    +   ...
    +   x ≡ an (mod mn)

-   Trong đó các m1, m2, ..., mn là các số nguyên tố cùng nhau đôi một, a1, a2, ..., an là các số nguyên và x là nghiệm cần tìm.

-   Ví dụ sau đây bạn đọc phát hiểu luôn :v
    +   Ta cần tìm x sao cho

    +   ![](https://i.imgur.com/qeY6sqy.png)
    +   Gọi các giá trị tương ứng sau đây:
        +   x ≡ a1 (mod m1)
        +   x ≡ a2 (mod m2)
        +   x ≡ a3 (mod m3)
    +   Và cách giải 
    +   Bước 1, ta cần tính các giá trị của M
        +   M = m1 * m2 * m3
        +   M1 = m2 * m3
        +   M2 = m1 * m3
        +   M3 = m1 * m2
    +   Bước 2, ta cần tính yi = inverse(Mi, mi)
        +   y1 = inverse(M1,m1)
        +   y2 = inverse(M2,m2)
        +   y3 = inverse(M3,m3)
    +   Khi đó, x ≡ (a1 * M1 * y1 + a2 * M2 * y2 + a3 * M3 * y3) (mod M)
    ![](https://i.imgur.com/F5fNVHm.png)

-   Đoạn code để giải bài này như sau:
```
m1, m2, m3 = 5, 11, 17  # gán giá trị m1, m2, m3 bằng 5, 11, 17
a1, a2, a3 = 2, 3, 5  # gán giá trị a1, a2, a3 bằng 2, 3, 5

M = m1*m2*m3  # tính giá trị M bằng tích của m1, m2 và m3
M1 = m2*m3  # tính giá trị M1 bằng tích của m2 và m3
M2 = m3*m1  # tính giá trị M2 bằng tích của m3 và m1
M3 = m1*m2  # tính giá trị M3 bằng tích của m1 và m2

x1 = inverse(M1, m1)  # tính giá trị nghịch đảo của M1 theo mod m1
x2 = inverse(M2, m2)  # tính giá trị nghịch đảo của M2 theo mod m2
x3 = inverse(M3, m3)  # tính giá trị nghịch đảo của M3 theo mod m3

# tính giá trị x bằng phương trình sử dụng định lý đồng dư Trung Hoa
x = (a1*M1*x1+a2*M2*x2+a3*M3*x3) % M


print(x)  # in ra giá trị của x

```
***Flag của bài này là: 872***