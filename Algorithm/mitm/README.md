## **MEET IN THE MIDDLE**
MITM hay **chia đôi tập** là một kỹ thuật tìm kiếm được sử dụng khi đầu vào nhỏ nhưng không đủ nhỏ để có thể dùng back_tracking.

## METHOD 
1. Đặt K = N / 2 
2. Chia N phần tử thành 2 tập: 
    - Tập X: gồm K phần tử đầu tiên. 
    - Tập Y: gồm tất cả các phần tử còn lại.
3. Quay lui ở tập X và lưu tổng của tất cả tập con vào mảng A. 
   Tương tự, quay lui ở tập Y và lưu tổng của tất cả phần tử vào mảng B. 
4. Kết hợp hai mảng A và B: 
    - Cách 1: lặp qua từng phần tử của A, với mỗi phần tử, duyệt qua tất cả các phần tử của B 
    - Cách 2: Sắp xếp cả hai mảng A và B sau đó dùng kỹ thuật hai con trỏ. 