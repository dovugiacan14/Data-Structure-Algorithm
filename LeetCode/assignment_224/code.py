from collections import deque, Counter



def basic_calculate(s):
    """IDEA
    - Nếu là số -> đọc hết số nguyên (có thể nhiều chữ số) -> cộng / trừ vào kết quả hiện tại.
    - Nếu là '+' hoặc '-' -> cập nhật dấu hiện tại.
    - Nếu là "(" -> đẩy kết quả hiện tại và dấu hiện tại vào stack -> reset kết quả.
    - Nếu là ")" -> kết thúc một biểu thức con -> lấy dấu và kết quả trước đó từ stack ra -> tính kết quả tổng thể.
    """
    stack = []
    num = 0
    result = 0
    sign = 1

    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result += sign * num
            continue

        elif char == "+":
            sign = 1
        elif char == "-":
            sign = -1
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ")":
            result = result * stack.pop() + stack.pop()
        i += 1
    return result
