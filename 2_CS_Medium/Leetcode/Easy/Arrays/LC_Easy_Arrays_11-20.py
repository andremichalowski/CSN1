1. 121 - BEST TIME TO BUY AND SELL STOCK (Prices. Find best day to buy and then sell.):

  def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

