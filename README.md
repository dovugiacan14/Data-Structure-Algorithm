# DATA STRUCTURE AND ALGORITHM 
Repository này tổng hợp lại những kiến thức về lập trình Python và một số bài code trên Leet Code nhằm mục đích ôn luyện và lưu lại kiến thức. 

## 1. Tổng quan về Cấu trúc dữ liệu: 
- **Cấu trúc dữ liệu:** là cách tổ chức, quản lý và lưu trữ dữ liệu một cách hiệu quả để có thể thuận tiện cho việc truy cập và điều chỉnh dữ liệu. Nó giúp tối ưu hóa các thao tác xử lý dữ liệu như tìm kiếm, chèn, xóa, hay sắp xếp. 

- **Giải thuật**: là một tập hợp các bước được xác định rõ ràng để giải quyết một vấn đề cụ thể. (step-by-step instructions).

Có 3 loại CTDL chính: 
- CTDL lưu trữ: thường có các thao tác như thêm, xóa, tìm kiếm phần tử. (Array, Linked list, Stack, Queue, Deque, Binary Search Tree, Hash Table,...)
- CTDL truy vấn: thường dùng cho các bài toán cần duy trì một tập hợp các số và thực hiện một số truy vấn trên đó. (Prefix Sum, Disjoint Sets, Sparse Table, Segment Tree, Fenwick, Heavy-light Decomposition, Persistent Data Structures)
- CTDL xâu: dùng cho các bài toán **xử lý xâu.** (Ex: Trie, Suffix array, Suffix Automaton, Palindrome Tree)

## 2. Các kiểu dữ liệu căn bản: 

| Tiêu chí              | **List** | **Set** | **Dict** | **Tuple** | 
| :------| :------- | :------- |:------- |:------- |
| Đặc điểm chính | List có thể thay đổi, có thứ tự | Tập hợp các giá trị duy nhất, không có thứ tự  | Cặp key-value, không có thứ tự  | Danh sách bất biến, có thứ tự  |
| Khả năng thay đổi | Mutable (có thể thay đổi) | Mutable (value có thể thay đổi, không có vị trí)  | Mutable (cặp key-value có thể thay đổi)  | Immutable (không thay đổi)  |
| Truy cập |Truy cập qua chỉ số (index) | Không hỗ trợ chỉ số (index)  | Truy cập qua key | Truy cập qua chỉ số (index) |
| Tính duy nhất |Không yêu câu giá trị duy nhất | Chỉ chứa các giá trị duy nhất | Key là duy nhất, value có thể lặp lại | Không yêu câu giá trị duy nhất |
| Hiệu quả |Tìm kiếm chậm hơn so với set/dict | Tìm kiếm nhanh hơn với phép hash | Tìm kiếm nhanh với key hash | Tìm kiếm chậm hơn so với set/dict |
| Ứng dụng phổ biến |Lưu trữ danh sách dữ liệu theo thứ tự | Xóa giá trị trùng lặp, kiểm tra tồn tại | Mapping key-value | Lưu trữ dữ liệu không thay đổi |
| Cú pháp khởi tạo |[1, 2, 3] | {1, 2, 3} | {"a": 1, "b": 2} | (1, 2, 3) |
| Hỗ trợ lặp (loop) |Có thể lặp qua từng phần tử | Có thể lặp qua từng phần tử | Lặp qua key hoặc key-value | Có thể lặp qua tưng phần tử |
| Sắp xếp | Có thể sắp xếp | Không sắp xếp được | Không sắp xếp trực tiếp (key được hash) | Không thể sắp xếp.  |

