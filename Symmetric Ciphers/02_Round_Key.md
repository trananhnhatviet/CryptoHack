# Round Key

![](https://i.imgur.com/IXlSfuo.png)

-   Chall này cho ta hiểu làm thế nào để Add_round_key trong AES
-   Thực chất, ta chỉ cần lấy từng phần tử của Matrix trạng thái, XOR với ma trận Round, ta sẽ thu được ma trận sau khi Add_round_key
-   Đoạn code ban đầu của chall như sau:
```
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    ???


print(add_round_key(state, round_key))


```
-   Ta cần hoàn thành function add_round_key bằng cách sử dụng 2 vòng for để có thể lần lượt XOR phần tử của state với round_key
-   Thuật toán sẽ như sau:
```
def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j]=s[i][j]^k[i][j] #must xor
    return s
```
-   Hoặc có thể sẽ như sau:
```
def add_round_key(s, k):
    return [[sss^kkk for sss, kkk in zip(ss, kk)] for ss, kk in zip(s, k)]
```
-   Sau khi add_round_key, ta cần dùng hàm matrix2bytes để lấy flag

-   Đoạn code cụ thể sẽ như sau:
```
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j]=s[i][j]^k[i][j] #must xor
    return s
            

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    s=""
    for i in matrix:
        for j in i:
            s=s+chr(j)
    return s

print(matrix2bytes(add_round_key(state, round_key)))

```
***Flag của bài là: crypto{r0undk3y}***