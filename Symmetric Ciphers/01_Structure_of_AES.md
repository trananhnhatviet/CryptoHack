# Structure of AES
![](https://i.imgur.com/xiaYAOf.png)
-   Chall này giúp ta biết cách chuyển từ 1 đoạn bytes thành 4 phần mỗi phần rồi xếp thành 1 ma trận 4x4, mỗi cột là 4 bytes và biết cách chuyển ngược lại
-   Đoạn code ban đầu như thế này:
```
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    ????

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))

```
-   Hiện tại ta cần hoàn thành function ``matrix2bytes`` để tìm được flag
-   ``bytes2matrix`` là 1 hàm chia 1 đoạn bytes thành 4 phần

-   Nhiệm vụ của ta là phải biết cách chuyển lại

-   Ta thấy dòng đầu tiên, 99 = 'c', 114 = 'r', 121 = 'y', 112 = 'p' --> ta sẽ dùng thuật toán như sau:
```
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    s=""
    for i in matrix:
        for j in i:
            s=s+chr(j)
    return s
```
-   Hoặc có thể sử dụng hàm này:
```
def matrix2bytes_2(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

```
-   Đoạn code cụ thể sẽ như sau:
```
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    s=""
    for i in matrix:
        for j in i:
            s=s+chr(j)
    return s


def matrix2bytes_2(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes_2(matrix))
```

***Flag của bài này là: crypto{inmatrix}***