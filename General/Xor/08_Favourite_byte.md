# **#Favourite byte**

![](https://i.imgur.com/DEE1Eub.png)


-   Mô tả: Chall này sẽ giúp chúng ta trau dồi thêm về các kiến thức cơ bản về Bytes, Xor và tìm hiểu thêm về định dạng của crypto trong Python là gì

-   Đề cho ta 1 đoạn mã hexa data='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d' 

-   Ta phải unhexlify đoạn data này và ra được 1 đoạn bytes

-   Ta chuyển đoạn này qua mã Decimal và được một list data

-   Vì đề có cho "I've hidden some data using XOR with a single byte, but that byte is a secret." nhưng ta không biết trong khoảng [0,255] là gồm những byte nào, nên ta cho i vào range(256)

-   Ta xor i với từng giá trị trong data, rồi lưu vào 1 biến string(biến này sẽ bị làm mới khi đổi giá trị i)

-   Khi thu được string, ta thêm 1 lệnh *if 'crypto' in string: * 'crypto' chính là format của mật mã

-   Nếu True thì output sẽ là Flag của Chall


-   Đoạn code sẽ như sau:
```

    from binascii import unhexlify

    inp = unhexlify('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

    data=[]

    for i in string:
        data.append(i)

    for i in range(256):
        a=""
        for j in data:
            a=a+chr(j^i)
        if "crypto" in a:
            print(a)

```

-   Và cờ của bài này là: ***crypto{0x10_15_my_f4v0ur173_by7e}***
