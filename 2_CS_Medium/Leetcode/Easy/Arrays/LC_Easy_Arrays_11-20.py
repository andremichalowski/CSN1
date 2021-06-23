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

3. 136 - SINGLE NUMBER (Find the single number in an arr of duplicates (Linear runtime, const extra space)):
  
  def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

4. 163 - Missing Ranges ()

  def findMissingRanges(self, nums, lower, upper):
    def getRange(lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
    ranges = []
    pre = lower - 1
    
    for i in xrange(len(nums) + 1):
        if i == len(nums):
            cur = upper + 1
        else:
            cur = nums[i]
        if cur - pre >= 2:
            ranges.append(getRange(pre + 1, cur - 1))
            
        pre = cur
        
    return ranges

5. 167 - Two Sum II - Input array is sorted (Numbers. Find two int that add to target):

  # Dictionary
  def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
  
  # two-pointer
  def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1

  # binary search        
  def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1

6. 169 - MAJORITY ELEMENT(nums. Find n the majority element.):
  class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]

  def majorityElement2(self, nums):
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums)//2:
            return n

  def majorityElement(self, nums):
    candidate, count = nums[0], 0
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate

7. 170 - TWO SUM III:

8. 204 - COUNT PRIMES (Count the number of prime numbers less than n):

    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)

9. 217 - CONTAINS DUPLICATE (Nums. dupes ? true : false):

    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))