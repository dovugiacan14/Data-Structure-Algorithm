# Linked List and Array 
Trong phần này. chúng tôi sẽ giới thiệu về danh sách liên kết (**linked list**) và mảng (**array**).

### **1. Array:** 
**Là một danh sách có chiều dài cố định** 

Ưu điểm: 
- Hữu ích với các bài toán đã biết trước số lượng phần tử. 
- Có thể truy cập phần tử của mảng một cách ngẫu nhiên bằng chỉ số. 

### **2. Linked List:** 
**Được hiểu đơn giản là một con trỏ, trỏ đến một node dữ liệu.** 

Đặc điểm: 
- Mỗi node dữ liệu cần có: data và một con trỏ, để trỏ đến node tiếp theo. 
- Không cố định, dễ thêm, xóa, thay đổi phần tử và thay đổi kích thước. 
- Thích hợp cho các bài toán chưa biết kích thước dữ liệu hoặc dữ liệu hay xáo trộn.  

| Tiêu chí              | **Linked List** | **Array** |
| :---------------- | :------ | :---- |
| Cấu trúc lưu trữ        |   Danh sách liên kết gồm các nút, mỗi nút chứa dữ liệu và con trỏ tới nút tiếp theo.   | Mảng là cấu trúc liên tục trong bộ nhớ, lưu các phần tử liên tiếp.  |
| Truy cập phần tử         |   Phải duyệt qua từng nút để truy cập phần tử tiếp theo (ĐPT: O(n))   | Truy cập trực tiếp bằng chỉ số (0(1)) |
| Chèn / xóa     |  - O(1): nếu chèn/xóa ở đầu hoặc cuối danh sách.    | - O(n): đề chèn hoặc xóa thì cần phải dời phần tử liền kề |
|     |  - O(n): nếu chèn/xóa ở giữa danh sách.    |  |
| Kích thước |  Linh hoạt, không cố định   | Cố định |
| Bộ nhớ |  Tiêu tốn nhiều bộ nhớ vì cần phải lưu con trỏ   | Hiệu quả hơn vì chỉ lưu giá trị phần tử |

