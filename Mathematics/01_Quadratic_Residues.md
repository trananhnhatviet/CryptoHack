# **Modular Square Root**

![](https://i.imgur.com/dqrgpPD.png)

-   Chall này giúp ta hiểu về thuật ngữ Quadratic Resides là gì, non-Quadratic Resides là gì và làm sao để biết nó là Quadratic Resides hay không
-   Quadratic Residue trong tiếng Việt được dịch là "Số bình phương dư". Nó là thuật ngữ trong toán học, thường được sử dụng để chỉ một số nguyên x trong phạm vi của một số nguyên tố p, mà có thể là kết quả của phép bình phương của một số nguyên trong phạm vi đó.

-   Nói cách khác, một số nguyên x được gọi là số bình phương dư modulo p nếu có một số nguyên x trong phạm vi của p sao cho x^2 ≡ a (mod p). Nếu không có số nguyên x nào thỏa điều kiện trên, thì số a được gọi là số bình phương không dư (quadratic non-residue).
-   Ví dụ, ta có p = 29, a = 11, ta cho x chạy từ (1 --> p-1), ta tìm được x = 5, với x^2 ≡ a (mod p) hay a ≡ x^2 (mod p) ---> a = 11 là 1 quadratic resides với p = 29
-   Trường hợp ta không tìm được x (1 --> p-1) sao cho x^2 ≡ a (mod p) hoặc a ≡ x^2 (mod p) ---> a là non quadratic resides

-   Trong chall này, ta có được p = 29, và 1 dãy các số nguyên bao gồm 2 số non quadratic resides và 1 số quadratic resides. Nhiệm vụ của chúng ta là tìm được x (1 <= i <= 28), sao cho x^2 ≡ a (mod p) hay a ≡ x^2 (mod p) với a là quadratic resides trong dãy số.

-   Đoạn code sẽ như sau:
```
p = 29
list_of_nums = [14, 6, 11]

#Dùng 1 vòng lặp từ 1 -- > p-1
for x in range(1,p):

    #Nếu x^2 mod p = 1 phần tử trong ints
    if pow(x, 2, p) in list_of_nums:

        #Hiển thị ra i và số quadratic resides
        print(x, pow(x,2,p))

#Output: (8,6) và (21,6)
```
***Vậy flag của bài này là số nhỏ hơn: 8***