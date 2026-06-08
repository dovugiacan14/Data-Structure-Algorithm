def max_profit_v3(prices):
    trans1, trans2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0 

    for i in prices: 
        trans1 = min(trans1, i)
        profit1 = max(profit1, i - trans1)

        trans2 = min(trans2, i - profit1)
        profit2 = max(profit2, i - trans2)

    return profit2
