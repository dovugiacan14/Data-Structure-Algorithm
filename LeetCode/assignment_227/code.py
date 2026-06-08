from collections import deque, Counter



def basic_calculate_II(s):
    s = s.replace(" ", "")
    stack = []
    num = 0
    sign = "+"

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    prev = stack.pop()
                    result = int(prev / num) if prev * num >= 0 else -(-prev // num)
                    stack.append(result)
                sign = ch
                num = 0
    return sum(stack)
