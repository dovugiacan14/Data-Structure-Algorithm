

def roman_to_int(s):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = (
        s.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )
    arr = []
    for i in s:
        arr.append(i)
    for idx in range(len(arr)):
        arr[idx] = int(dic[arr[idx]])
    return sum(arr)
