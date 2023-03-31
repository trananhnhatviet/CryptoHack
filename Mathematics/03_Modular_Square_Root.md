# **Modular Square Root**

![](https://i.imgur.com/LI9dQHP.png)



-   Chall này cho ta biết được Thuật toán Tonelli-Shanks, các bước giải và mục đích của nó là gì.
-   Tonelli - Shanks, 1 thuật toán dùng để tìm x thỏa mãn x^2 ≡ a (mod p), với a và p cho trước.
-   Như bài trước, ta có thể dùng công thức là x = pow(a,(p+1)//4,p) để tìm được x, thế nhưng, p phải có dạng là 4k + 3, thế nhưng ở bài này, p có dạng là 4k + 1, thì dùng công thức thì p + 1 sẽ không chia hết cho 4, thế nên ta phải dùng thuật toán này.
-   Các bước của thuật toán sẽ như sau:
    +   Trước hết, a phải là Quadratic resides của p, nếu không thì thoát
    +   Phân tích p-1 thành dạng 2^e * s, và s sẽ là số lẻ
    +   Tìm 1 số n, sao cho n là non Quadratic resides của p
    +   Áp dụng công thức chính của thuật toán, gán các giá trị:
        +   x = pow(a, (s + 1) // 2, p)
        +   b = pow(a, s, p)
        +   g = pow(n, s, p)
        +   r = e
    +   Sử dụng vòng lặp cho tới khi return ra kết quả:
        +   Tìm một số nguyên m sao cho t^(2^m) mod p = 1 (m in range(r))
        +   Nếu m = 0, kết quả đã tìm được là x
        +   Nếu không thì:
            +   Tính giá trị mới của các biến
            +   gs = pow(g, 2 ** (r - m - 1), p)
            +   g = (gs * gs) % p
            +   x = (x * gs) % p
            +   b = (b * g) % p
            +   r = m
        
Đoạn code sẽ như sau:
```
from Crypto.Util.number import inverse 


def square_root(a, p):
    # Tonelli–Shanks algorithm

    # Kiểm tra xem a có phải là quadratic residues của p hay không
    if legendre_symbol(a, p) != 1:
        return 0
    # Nếu a = 0 hoặc p = 2 thì kết quả là 0
    elif a == 0 or p == 2:
        return 0
    # Nếu p có dạng là 4k+3 thì áp dụng công thức tương ứng
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Tìm s và q sao cho p - 1 = (2^e)*s
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Tìm một số nguyên n sao cho n là non quadratic residues của p
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Áp dụng công thức chính của thuật toán
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        # Tìm một số nguyên m sao cho t^(2^m) mod p = 1
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        # Nếu m = 0, kết quả đã tìm được là x
        if m == 0:
            return x

        # Tính giá trị mới của các biến
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):

    ls = pow(a, (p - 1) // 2, p)
    if ls == p-1:
        return -1
    else:
        return ls


a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161


print(square_root(a, p))

```

***Flag của bài này là: 2362339307683048638327773298580489298932137505520500388338271052053734747862351779647314176817953359071871560041125289919247146074907151612762640868199621186559522068338032600991311882224016021222672243139362180461232646732465848840425458257930887856583379600967761738596782877851318489355679822813155123045705285112099448146426755110160002515592418850432103641815811071548456284263507805589445073657565381850521367969675699760755310784623577076440037747681760302434924932113640061738777601194622244192758024180853916244427254065441962557282572849162772740798989647948645207349737457445440405057156897508368531939120***