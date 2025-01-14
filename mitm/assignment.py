from itertools import product
from bisect import bisect_right

"""Assigment 1: Bài toán Cái túi 

Cho N cục món đồ, mỗi món đồ có trọng lượng W_i và giá trị V_i. 
Bạn có một cái túi có tải trọng tối đa là M. Hỏi tổng giá trị vàng lớn nhất 
có thể thu được mà không làm rách túi. 

"""
def get_item(total_item, max_weight): 
    w = [0] * total_item 
    v = [0] * total_item
    B = []
    sumWA = []
    sumVA = []

    def try_X(i, sumW, sumV):
        if sumW > max_weight: 
            return 
        if i > total_item // 2: 
            sumWA.append(sumW)
            sumVA.append(sumV)
            return 
        try_X(i + 1, sumW, sumV)
        try_X(i + 1, sumW + w[i], sumV + v[i])
    
    def try_Y(i, sumW, sumV):
        if sumW > max_weight:
            return 
        if i > total_item: 
            B.append((sumW, sumV))
            return 
        try_Y(i + 1, sumW, sumV)
        try_Y(i + 1, sumW + w[i], sumV + v[i])

    try_X(1, 0, 0)
    try_Y(total_item//2 + 1, 0, 0)

    B.sort()
    sumWB = [0] * len(B)
    maxSumWB = [0] * len(B)

    for i in range(len(B)):
        sumWB[i] = B[i][0]
        maxSumWB[i] = max(maxSumWB[i - 1] if i > 0 else 0, B[i][1])

    maxValue = 0 
    for i in range(len(sumVA)):
        remaining_weight = max_weight - sumWA[i]
        j = bisect_right(sumWB, remaining_weight) - 1
        if j >= 0: 
            maxValue = max(maxValue, sumVA[i] + maxSumWB[j])
    return maxValue