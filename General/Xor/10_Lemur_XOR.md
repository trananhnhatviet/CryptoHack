# **#You either know, XOR you don't**

![](https://i.imgur.com/BSfqnAv.png)


-   Đoạn code sẽ như sau:
```

from binascii import unhexlify

with open("lemur.png", mode='rb') as fl:
    lemur = fl.read()
    

with open("flag.png", mode='rb') as ff:
    flag = ff.read()

d = b''
for b1, b2 in zip(lemur, flag):
    d += bytes([b1^b2])

with open("new.png", mode='wb') as fn:
    fn.write(d)
    
    
```
-   Khi đó ảnh sẽ là: 
    ![](https://i.imgur.com/xfC7zHe.png)

-   Và cờ của bài này là: ***crypto{X0Rly_n0t!}***
