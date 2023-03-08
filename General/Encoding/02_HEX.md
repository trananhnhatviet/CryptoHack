# ***#HEX***

![](https://i.imgur.com/569bl0o.png)


-    Mô tả: Mục đích của chall này giúp chúng ta biết cách chuyển từ Hex qua Bytes và ngược lại bằng các hàm:
     +    bytes.fromhex(): Chuyển từ hex sang bytes
     +    bytes.hex()    : Chuyển từ bytes sang hex
-    Ngoài ra, còn 1 cách khác để chuyển từ bytes sang hexa và ngược lại bằng cách:
     +    from Binascii import hexlify, unhexlify //cài thư viện
     +    unhexlify()    : Chuyển từ hex sang bytes
     +    hexlify()      : Chuyển từ bytes sang hex
         

-    Ta thấy đề bài cho 1 đoạn data:
     `63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
     

-    Ta cần chuyển mã này qua Bytes bằng câu lệnh: bytes.fromhex(data) hoặc unhexlify()

-    Đoạn code sẽ như sau:
```
     data='63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
     flag=bytes.fromhex(data).decode()
     print(flag)    
     #Chạy đoạn code, chương trình sẽ đưa ra output: b'crypto{You_will_be_working_with_hex_strings_a_lot}' là dưới dạng bytes
```
Hoặc
```
     from binascii import unhexlify
     data='63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
     print(unhexlify(data))

```
     
-    Và cờ của bài này là: ***crypto{You_will_be_working_with_hex_strings_a_lot}***

-    (Tìm hiểu thêm tại đây: [https://en.wikipedia.org/wiki/Hexadecimal])