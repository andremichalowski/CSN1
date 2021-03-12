1. CLIMBING STAIRS:

  def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev1 = 1
        prev2 = 2
        current = 0
        for i in range(2, n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current

2. BEST TIME TO BUY AND SELL STOCK:

  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
      return 0

    maxProfit = 0
    minPurchase = prices[0]
    for i in range(1, len(prices)):		
      maxProfit = max(maxProfit, prices[i] - minPurchase)
      minPurchase = min(minPurchase, prices[i])
    return maxProfit


3. MAXIMUM SUB ARRAY: (KADANES ALGORITHM):

  for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

