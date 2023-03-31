# **Vector**

![](https://i.imgur.com/eoObuSg.png)


-   Chall này cho ta biết được cách tính giữa các Vector với nhau

-   Để có thể thực hiện được các phép xử lý vector, ta cần phải sử dụng thư viện numpy
-   Thực chất, các vector đều là những mảng, những dãy số, thế nên, ta cần phải biến đổi nó thành vector. Ví dụ:
    +   Ta muốn có 1 vector a = (1,2,3) thì ta phải xử lý như sau:
        +   ``import numpy as np``
        +   ``x = [1,2,3]``
        +   ``a = np.array(x)`` --> Thu được vector a
-   Các phép cộng trừ nhân chia thì ta sử dụng bình thường như là các biến số, thế nhưng, vector còn có khái niệm Tích vô hướng (dot), thế nên để lấy tích vô hướng của 2 vector a và b, ta làm như sau:
    +   ``result = np.dot(a,b)``

-   Code của bài này sẽ như sau:
```
import numpy as np

v = [2,6,3]
w = [1,0,0]
u = [7,7,2]

A = np.array(v)
B = np.array(w)
C = np.array(u)

X = 3*(2*A - B)
Y = 2*C
result = np.dot(X,Y)
print(result)
```
***Flag của bài này là: 702***