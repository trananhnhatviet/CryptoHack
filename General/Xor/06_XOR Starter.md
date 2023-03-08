# **XOR Starter**

![](https://i.imgur.com/chPKnJD.png)

-   Mô tả: Chall này sẽ giúp chúng ta hiểu cơ bản Xor là gì, ký hiệu của Xor và biết cách Xor giữa 2 biến

-   Ta thấy đề cho dữ liệu là 1 string là: data="label"
-   Đề hướng dẫn ta Xor từng kí tự của data cho 13
    Để hiểu bản chất, ta đổi 13 ra bin
    '''
        bin13=(bin(13)[2:])
    '''
    và bin13=00001101
-   Tiếp theo ta đổi từng kí tự của data ra decimal rồi ra bin
    '''
        #ví dụ với 'l'
        #'l' trong ascii đổi ra được là 108
        binl=(bin(108)[2:])
    '''
    và binl=01101100
      bin13=00001101
      
-   Ta xor binl với bin13 ta được 01100001 đổi ra decimal là 49 và sang Ascii là 'a'
-   Tương tự với các kí tự khác trong data
-   Đoạn code sẽ như sau:
``` 
    data='label'
    flag=""
    for i in data:
        flag=flag+chr(ord(i)^13)
    print('crypto{'+flag+'}')
```
-    Và cờ của bài này là: ***crypto{aloha}***


