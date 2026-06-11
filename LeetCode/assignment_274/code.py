def hIndex(citations): 
    citations.sort(reverse=True)
    h = 0 
    for i, cite in enumerate(citations): 
        if cite >= i + 1: 
            h = i + 1
        else:
            break 
    return h


def hIndex2(citations):
    new_citations = reversed(citations)
    h = 0 
    for i, cite in enumerate(new_citations): 
        if cite >= (i + 1): 
            h += 1 
        else: 
            break 
    return h 
