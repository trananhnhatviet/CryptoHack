# **Gram Schmidt**

-   Chall này giúp ta hiểu được Trực giao là gì, và cách trực giao 1 vector làm sao:
-   Cơ sở trực giao của một vector là một tập hợp các vector tạo thành một hệ cơ sở trực giao, có các tính chất sau đây:

    +   Các vector trong hệ cơ sở trực giao là tương đương và không có vector nào là một tuyến tính kết hợp của các vector khác trong hệ.
    +   Các vector trong hệ cơ sở trực giao đều có độ dài bằng nhau.
    +   Hai vector bất kỳ trong hệ cơ sở trực giao đều vuông góc với nhau.
-   Để tìm cơ sở trực giao của một vector, chúng ta có thể sử dụng phương pháp Gram-Schmidt. Phương pháp này bắt đầu bằng cách chọn một vector bất kỳ trong không gian và đưa nó vào hệ cơ sở trực giao. Sau đó, chúng ta chọn vector thứ hai bằng cách trừ đi phần chiều của vector thứ nhất trên vector đó, và tiếp tục thực hiện quá trình này để tìm ra các vector còn lại trong hệ cơ sở trực giao.
-   Thuật toán sẽ như thế này:
![](https://i.imgur.com/uN60Epu.png)

-   Chall này bắt ta tìm cơ sở trực giao của hệ vector ``v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5)`` và flag sẽ là phần tử thứ 2(làm tròn số thập phân thứ 5) của vector v4 sau khi đã thực hiện trực giao

-   Code của bài này sẽ như sau:
```
import numpy as np

# Định nghĩa hàm gram_schmidt với đầu vào là tập hợp vectors và vector đầu tiên v1
def gram_schmidt(vectors, v1):

    # Tạo một danh sách các vector cơ sở với vector đầu tiên là v1
    basis = []
    basis.append(v1)

    # Lặp qua tất cả các vector còn lại trong tập hợp vectors
    for v in vectors:

        # Lặp qua tất cả các vector cơ sở trong danh sách basis
        for b in basis:

            # Áp dụng công thức Gram-Schmidt để biến đổi vector v
            v = v - np.dot(v, b) / np.dot(b, b) * b

        # Thêm vector mới đã được biến đổi vào danh sách basis
        basis.append(v)

    # Trả về danh sách các vector cơ sở đã được chuẩn hóa
    return basis

# Khởi tạo các vector đầu vào
v1 = np.array([4, 1, 3, -1])
v2 = np.array([2, 1, -3, 4])
v3 = np.array([1, 0, -2, 7])
v4 = np.array([6, 2, 9, -5])

# Tạo tập hợp các vector
vectors = [v2, v3, v4]

# Áp dụng phương pháp Gram-Schmidt với vector đầu tiên là v1 và tập hợp các vector vectors
basis = gram_schmidt(vectors, v1)

# In ra các vector cơ sở đã được chuẩn hóa
for i, v in enumerate(basis):
    print(f"v{i+1} = {v}")

```

***Flag của bài này là: 0.96161***