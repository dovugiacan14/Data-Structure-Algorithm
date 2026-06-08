
def fraction_to_decimal(numerator, denominator):
    if numerator == 0: 
        return "0"

    res = []
    
    # handle sign 
    if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
        res.append("-") 
    numerator = abs(numerator)
    denominator = abs(denominator)

    # whole part 
    res.append(str(numerator // denominator))
    remainder = numerator % denominator 

    if remainder == 0: 
        return "".join(res)
    
    # map remainder to its index in the result.
    remainder_map = {}
    while remainder_map != 0: 
        if remainder in remainder_map: 
            index = remainder_map[remainder]
            res.insert(index, "(")
            res.append(")")
            break 
            
        remainder_map[remainder] = len(res)
        remainder *= 10 
        res.append(str(remainder // denominator))
        remainder %= denominator 
    return "".join(res)
