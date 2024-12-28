## Overview 

### 1. Bubble Sort 

- **Idea:** so sánh hai phần tử liên tiếp, nếu phần tử sau nhỏ hơn phần tử trước thì hoán đổi vị trí của chúng. 

- **Độ phức tạp:** O($N^2$)
- **Ưu điểm:** code đơn giản, dễ hiểu, không tốn bộ nhớ. 

### 2. Insertion Sort 

- **Idea:** sắp xếp lần lượt từng đoạn gồm một phần tử đầu tiên, hai phần tử đầu tiên,..., N phần tử đầu tiên.  

- **Độ phức tạp:** O($N^2$)
- **Đơn giản nhất:** mảng đã có thứ tự.
- **Phức tạp nhất:** mảng có thứ tự ngược hoàn toàn với thứ tự muốn sắp xếp.  

### 3. Selection Sort 
- **Idea:** chọn phần tử nhỏ nhất trong mảng hiện tại, đặt vào đầu mảng mới và loại bỏ ra khỏi mảng cũ. 
- **Độ phức tạp:** O($N^2$)  

### 4. Mergre Sort 
- **Idea:** được chia làm 3 bước 

    * B1: Chia dữ liệu thành 2 phần và sắp xếp từng phần 
    * B2: Tạo một dãy A mới để chứa các phần tử đã sắp xếp. 
    * B3: So sánh hai phần tử đầu tiên của hai phần. Phần tử nào nhỏ hơn thì ta cho vào chính và xóa khỏi phần tương ứng. 
- **Độ phức tạp:** O(n.log(n))

### 5. Heap Sort 
- **Idea:** tại mỗi bước, lấy phàn tử nhỏ nhất trong Heap cho vào mảng 
- **Độ phức tạp:** O(n.log(n))

### 6. Quick Sort
- **Idea:** chọn một phần tử bất kỳ làm pivot, những phần nào lớn hơn thì đưa về phải, phần nào nhỏ hơn pivot thì đưa về trái. Cuối cùng gọi đệ quy đế sắp xếp hai phần. 
- **Độ phức tạp:** O(n.log(n)) 


