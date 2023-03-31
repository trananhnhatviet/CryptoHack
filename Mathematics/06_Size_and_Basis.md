# **Size and Basis**

![](https://i.imgur.com/iaPZ2eV.png)



-   Chall này cho ta biết độc lập tuyến tính là gì, cơ sở vector là gì

-   Độc lập tuyến tính là như sau: 
![](https://i.imgur.com/FV7j0C9.png)    

-   Cơ sở của vector là như sau:
![](https://i.imgur.com/wEZNZGd.png)

-   Còn nếu bạn đọc mà không hiểu gì thì nên học lại Đại số tuyến tính nha :v

-   Bài này yêu cầu chúng ta tính chiều dài của Vector, hay còn ký hiệu là ||v||
-   Để tính được độ dài của vector v, ta có nhiều cách
    +   Ta dot(v,v) rồi căn bậc 2 ra
    +   Ta tính tổng bình phương từng phần tử trong vector rồi căn bậc 2
    +   Ta dùng hàm của numpy int(np.linalg.norm(v))
-   
-   Code của bài này sẽ như sau:
```
import numpy as np

v = np.array([4, 6, 2, 5])

print(int(np.linalg.norm(v)))
```
Hoặc
```
from numpy import *
v = array((4, 6, 2, 5))      
print(int(sqrt(dot(v,v))))
```

***Flag của bài này là: 9***