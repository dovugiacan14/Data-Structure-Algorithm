def count_and_convert(text): 
    if not text: 
        return ""
    
    result = []
    count = 1 
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else: 
            result.append(f"{count}{text[i - 1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    return "".join(result)

def count_and_say(n): 
    if n == 1: 
        return "1"
    return count_and_convert(count_and_say(n-1))
