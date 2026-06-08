

def intToRoman(num):
    num_str = str(num)
    n = len(num_str)
    arr_roman_part = []
    for idx, digit in enumerate(num_str, start=1):
        digit = int(digit)
        section_unit = n - idx
        if digit == 0:
            continue
        # thousand unit
        if section_unit == 3:
            text = "M" * digit
            arr_roman_part.append(text)
        # hundreds unit
        if section_unit == 2:
            if digit == 9:
                text = "CM"
            elif digit == 4:
                text = "CD"
            elif digit == 5:
                text = "D"
            elif digit == 1:
                text = "C"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "D" + "C" * offset
            else:
                text = "C" * digit
            arr_roman_part.append(text)
        # tenths unit
        if section_unit == 1:
            if digit == 1:
                text = "X"
            elif digit == 4:
                text = "XL"
            elif digit == 5:
                text = "L"
            elif digit == 9:
                text = "XC"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "L" + "X" * offset
            else:
                text = "X" * digit
            arr_roman_part.append(text)
        # unit
        if section_unit == 0:
            if digit == 1:
                text = "I"
            elif digit == 4:
                text = "IV"
            elif digit == 5:
                text = "V"
            elif digit == 9:
                text = "IX"
            elif digit > 5 and digit < 9:
                offset = digit - 5
                text = "V" + "I" * offset
            else:
                text = "I" * digit
            arr_roman_part.append(text)
    return "".join(arr_roman_part)
