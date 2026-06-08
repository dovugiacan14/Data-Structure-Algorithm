def letterCombination(digits): 
    encode_number_phone = {
        '2': 'abc', 
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []
    if not digits: 
        return result 
    
    def backtrack(combination, netx_digits):
        if not netx_digits:
            result.append(combination)
            return 
        
        for letter in encode_number_phone[netx_digits[0]]:
            backtrack(combination + letter, netx_digits[1:])
    backtrack("", digits)
    return result
