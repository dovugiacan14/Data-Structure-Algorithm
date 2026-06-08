
def max_profit(prices):
    res = 0 
    buy_value = prices[0]

    for price in prices[1:]:
        res = max(res, price - buy_value)
        buy_value = min(buy_value, price)
        
    return res 
