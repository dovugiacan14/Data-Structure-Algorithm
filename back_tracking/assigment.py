"""
BT1: Hãy liệt kê tất cả các dãy nhị phân có độ dài n, là dãy n ký tự và chỉ gồm cá ký tự 0, 1

Example: 
- Input: n = 3 

- Output: 000, 001, 010, 011, 100, 101, 110, 111
"""
def generate_string(start_pos, n, res_string, result):
    # Base case 
    if start_pos > n: 
        result.append(res_string)
        return 
    
    # Recursive 
    for i in ["0", "1"]:
        generate_string(start_pos + 1, n, res_string + i, result)

    return result

"""
BT2: Cho tập S = {1, 2, 3, ..., n}. Hãy in ra tất cả các tập con có chính xác k phần tử của S. 
Hai tập con là hoán vị của nhau thì chỉ tính là 1. 

"""
def create_arr(n):
    return [f"{i + 1}" for i in range(n)] 

def generate_subset(arr, pos, k, res_string, result):
    # base case 
    if len(res_string) == k: 
        result.append(res_string)
        return  
    
    # recursive 
    for i in arr:
        res_string += i
        generate_subset(arr, pos + 1, k, res_string, result)
        res_string = res_string[: -1]
    
    return result

"""
BT3: Bài toán phân tích số 

Ở một quốc gia có n loại tiền gồm các mệnh giá a1, a2, ... , an (n < 11). 
Có những cách nào để lấy các tờ tiền sao cho tổng mệnh giá của chúng là S. 
Biết rằng mỗi mệnh giá tiền có thể được lấy nhiều lần và hai cách lấy là hoán vị của nhau chỉ tính là một.

Example:
- Input:  
    - Với 3 mệnh giá tờ tiền: 10, 20, 50
    - Và tổng target là 100

- Output: 
    - Có 10 cách lấy
"""
def get_money_set(money_lst, target_total, index, cur_total, result):
    # base case 
    if sum(cur_total) == target_total: 
        result.append(list(cur_total))
        return 
    
    if sum(cur_total) > target_total: 
        return 
    
    # recursive 
    for i in range(index, len(money_lst)):
        cur_total.append(money_lst[i])
        get_money_set(money_lst, target_total, i, cur_total, result)
        cur_total.pop()
    
    return result

"""
BT4: Bài toán xếp hậu 

Tìm tất cả các cách xếp n (n <= 12) quân Hậu lên bàn cờ n x n sao cho không quân hậu nào có thể ăn được nhau. 
Nếu có hai cách là hoán vị của nhau (về vị trí) thì chỉ tính là một.

Điều kiện hai quân hậu A và B ăn nhau: 
- Khi A và B nằm cùng hàng: x_A = x_B 
- Khi A và B nằm cùng cột: y_A = y_B 
- Khi A và B nằm trên cùng đường chéo: 
    - x_A + y_A = x_B + y_B 
    - x_A - y_A = x_B - y_B

Ý tưởng: 
"""


if __name__ == "__main__": 
    # BT1 
    res = generate_string(1, 4, "", [])

    # BT2 
    arr = create_arr(5)
    res = generate_subset(
        arr= arr, 
        pos= 1, 
        k = 3, 
        res_string= "",
        result= []
    )

    # BT3 
    res = get_money_set(
        money_lst= [10, 20, 50],
        target_total= 100, 
        index= 0, 
        cur_total= [],
        result= []
    )
    print(res)
    print(len(res))

