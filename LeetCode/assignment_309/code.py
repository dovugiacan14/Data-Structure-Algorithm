def maxProfit(prices): 
    hold = -prices[0]
    sold = 0 
    rest = 0 

    for price in prices[1:]: 
        prev_hold = hold 
        prev_sold = sold 
        prev_rest = rest 

        hold = max(prev_hold, prev_rest - price)
        sold = prev_hold + price 
        rest = max(prev_rest, prev_sold) 
    return max(sold, rest) 

if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(maxProfit(prices)) 
    