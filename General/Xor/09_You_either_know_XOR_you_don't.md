# **#You either know, XOR you don't**

![](https://i.imgur.com/aUxb1jw.png)


-   Mô tả: Chall này sẽ giúp chúng ta sẽ vận dụng các tính chất của Xor 1 cách thành thạo hơn

-   Để Xor nhanh và tiện lợi hơn thì mình dùng thư viện pwn và import xor
    ```from pwn import xor```

-   Đề bài cho ta 1 đoạn mã Hexa 
    data='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

-   Ta cần chuyển mã này sang Bytes
        data=bytes.fromhex(data)
        Hoặc
        data=unhexlify(data)

-   Đề có nói: "I've encrypted the flag with my secret key, you'll never be able to guess it." nên ta có
            flag = data ^ key --> key = flag ^ data

-   Ngoài ra, ta thấy dạng của cờ là 'crypto{' nên ta gán
        flag = b'crypto{'

-   Và kết quả của phép xor giữa flag và data là: b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
        --> Ta đoán key là: key=b'myXORkey'

-   Cuối cùng, ta chỉ cần xor key với data, ta sẽ tìm được flag

-   Đoạn code sẽ như sau:
```

    from binascii import unhexlify
    from pwn import xor
    
    data = unhexlify('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
    
    flag=b'crypto{'
    
    key=xor(flag,data)
    print(key)
    key=b'myXORkey'
    flag=xor(key,data)
    print(flag)
    
```

-   Và cờ của bài này là: ***crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}***
