"""Assignment 121. Best Time to Buy and Sell Stock 

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    - Input: prices = [7,1,5,3,6,4]
    - Output: 5
    - Explaination:  Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

def max_profit(prices):
    res = 0 
    buy_value = prices[0]

    for price in prices[1:]:
        res = max(res, price - buy_value)
        buy_value = min(buy_value, price)
        
    return res 

"""Assignment 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
    - Input: prices = [7,1,5,3,6,4]
    - Output: 7
    - Explaination:  
        + Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        + Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        + Total profit is 4 + 3 = 7.
"""
def max_profit_v2(prices): 
    profit = 0 
    for i in range(1, len(prices)): 
        if prices[i] > prices[i-1]: 
            profit += prices[i] - prices[i-1]
    return profit

print(max_profit_v2([1,2,3,4,5]))

"""Assignment 123. Best Time to Buy and Sell Stock III.

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
    - Input: prices = [3,3,5,0,0,3,1,4]
    - Output: 6
    - Explaination:  
        + Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        + Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
def max_profit_v3(prices):
    trans1, trans2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0 

    for i in prices: 
        trans1 = min(trans1, i)
        profit1 = max(profit1, i - trans1)

        trans2 = min(trans2, i - profit1)
        profit2 = max(profit2, i - trans2)

    return profit2
