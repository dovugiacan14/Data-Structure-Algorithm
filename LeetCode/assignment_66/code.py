        
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number_str = "".join(map(str, digits))
    number = int(number_str)
    number += 1
    res = [] 
    for c in str(number): 
        res.append(int(c))
    return res
