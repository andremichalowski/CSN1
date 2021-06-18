1. 121 - BEST TIME TO BUY AND SELL STOCK (Prices. Find the max profit buying on one day and selling on another.):

  def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

2. 122 - BEST TIME TO BUY AND SELL STOCK 2 (Find the max profit of buying and selling on different days in Prices arr.):

  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        max_profit += max(prices[i+1] - prices[i], 0)
    return max_profit