## **Back Tracking**

Backtracking Tracking (**thuật toán quay lui**) là một kỹ thuật dựa trên đệ quy. 

Ý tưởng: 
- Tìm lời giải từng bước. 
- Mỗi bước chọn một trong số các lựa chọn có khả năng xảy ra và đệ quy. 

**Presudo Code**

```bash
def backtrack(pos):
    // trường hợp cơ sở 
    if (pos ở vị trí cuối cùng):
        if (output thỏa điều kiện): 
            return; 
    
    // phần đệ quy
    for (<tất cả các giá trị i có thể có ở vị trí pos>):
        <thêm giá trị i vào tập đang xét>
        backtrack(pos + 1)
        <xóa bỏ giá trị i khỏi tập đang xet>
```

