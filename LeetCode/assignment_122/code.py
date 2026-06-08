def max_profit_v2(prices): 
    profit = 0 
    for i in range(1, len(prices)): 
        if prices[i] > prices[i-1]: 
            profit += prices[i] - prices[i-1]
    return profit

print(max_profit_v2([1,2,3,4,5]))
