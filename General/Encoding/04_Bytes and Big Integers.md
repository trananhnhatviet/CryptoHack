# **#Bytes and Big Integers**


![](https://i.imgur.com/n6cevKE.png)



-   Mô tả: Chall này sẽ giúp chúng ta hiểu được câu lệnh long_to_bytes() và bytes_to_long():
    +   long_to_bytes(): Chuyển từ integer về bytes
    +   bytes_to_long(): Chuyển từ bytes sang integer
    Ví dụ:
    +   Ta có 
        *   data=b'abc'
        Ta muốn chuyển sang integer thì phải theo các bước:
        *   Chuyển từng kí tự của data về hex --> 616263
        *   Chuyển từ hex về binary --> 011000010110001001100011
        *   Chuyển từ binary về integer --> 6382179
        Thay vào đó, ta có thể sử dụng hàm bytes_to_long(data) thì sẽ ra được 6382179
    +   Còn long_to_bytes() thì ngược lại quá trình trên

-    Đoạn code sẽ như sau:
```
    from Crypto.Util.number import*

    data=11515195063862318899931685488813747395775516287289682636499965282714637259206269

    flag=long_to_bytes(data).decode()

    print(flag)
```
-    Và cờ của bài này là: ***crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}***


