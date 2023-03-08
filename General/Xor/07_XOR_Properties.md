# **#XOR Properties**

![](https://i.imgur.com/16H14y5.png)


-   Mô tả: Chall này sẽ giúp ta hiểu được các tính chất của Xor giữa 2 hoặc nhiều biến với nhau

-   Trước hết, ta phải hiểu các tính chất của Xor:
    +   a^b = b^a
    +   a^b = c --> a^c = b và b^c = a
    +   a^0 = a
    +   a^a = 0

-   Ta thấy đề bài cho 1 đoạn data:
```
    KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
    KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
    KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
    FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```
-   Ta có KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
==> KEY2 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ KEY1


-   Tương tự ta có 
    +   KEY3 = KEY2 ^ c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
    +   FLAG = KEY1 ^ KEY3 ^ KEY2 ^ 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

-   Vì các đoạn mã này đang dạng String và không có kiểu liệu nào hệ Hexa nên ta phải chuyển sang hết hệ Decimal để Xor vì thế khi có kết quả Xor của FLAG thì ta phải chuyển về lại hệ Hexa 

-   Khi chuyển FLAG về Hexa thì ta thấy 2 kí tự đầu '0x' không phải là hệ Hexa nên ta phải loại bỏ 2 kí tự này

-   Unhexlify(FLAG) và thu được cờ

-   Đoạn code sẽ như sau:
```
    from Crypto.Util.number import*
    from binascii import unhexlify

    def convert(a,b):
        return a^b

    k1=int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313',16)
    k2=int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e',16)
    k3=int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1',16)
    k4=int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf',16)

    key2=convert(k1,k2)

    key3=convert(key2,k3)

    flag=hex(convert(convert(convert(key3,key2),k1),k4))


    flag=flag[2:]

    print(unhexlify(flag).decode())

```

-   Và cờ của bài này là: ***crypto{x0r_i5_ass0c1at1v3}***
