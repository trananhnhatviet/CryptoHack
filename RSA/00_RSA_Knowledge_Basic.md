# **#RSA Knowledge Basic**

-   Chú ý: Kí tự '^' ở bài này sẽ là cấp số mũ chứ không phải là Xor

-   Trước hết, ta cần phải hiểu các định lý toán học Euler's
    +   Ký hiệu là φ hoặc là phi
    +   Lấy 1 số N và phân tích N thành các nhân tử nguyên tố: N = p1^k1 * p2^k2 * ... * pn^kn
    +   Ta có: φ(N) = (p1^(k1-1))(p1-1) * (p2^(k2-1))(p2-1) * ...* (pn^(kn-1))(pn-1)
    +   Ví dụ: Tính φ(20)
        +   N = 2 * 2 * 5 = 2^2 * 5
        +   φ(N) =  (2^(2-1)(2-1)) * (5^(1-1)*(5-1)) = 2 * 1 * 1 * 4 = 8



-   Giả sử có 1 cuộc hội thoại giữa Alice và Bob, ngoài ra còn có 1 kẻ nghe lén là Eve

-   Đầu tiên, Alice sẽ lấy 2 số nguyên tố là p, q và N = p*q

-   Tiếp theo là cần tính φ(N): phi = (p-1)(q-1)

-   Chọn 1 số e (e thường là 65537)

-   Và private key d = inverse(e,phi) hoặc là d = pow(e,-1,phi)

-   Hiện tại, Alice đang có p,q,N,e,phi,d và Alice chỉ gửi ra bên ngoài N và e

-   Khi đó, cả Eve và Bob đều nhận được

-   Trước hết, Alice gửi cho Bob 2 số là N và e (Eve cũng sẽ nhận được N và e)

-   Bob sẽ dùng N và e để mã hóa message mà mình muốn gửi thành: ciphertext = (message ^ e) mod N

-   Khi đó, Bob sẽ chuyển message muốn gửi thành bytes và chuyển nó sang integer

-   Và message ^ e mod N ≡ c và ciphertext = c

-   Tiếp theo Bob sẽ công khai ciphertext. Khi đó cả Eve và Alice đều nhận được

-   Với Alice:
    +   Khi có ciphertext rồi, Alice sẽ tìm được decrypted với decrypted = pow(ciphertext,d,N)
    +   Và chuyển decrypted thành bytes thì sẽ nhận được message
-   Với Eve:
    +   Chỉ có N, ciphertext, e VÀ KHÔNG CÓ PRIVATE KEY d --> Không làm được gì

-   Tất cả chỉ là theo mình hiểu được, còn nếu bạn giỏi tiếng Anh thì mình nghĩ bạn nên xem video này: https://www.youtube.com/watch?v=wXB-V_Keiu8