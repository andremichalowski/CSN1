# 1. REMOVE DUPLICATES:

# 2. BEST TIME TO BUY AND SELL STOCK:

3. ROTATE ARRAY:
  class Solution:
      def rotate(self, nums: List[int], k: int) -> None:
          # Input: list[int] + (int where rotates: k)
          # Output: list[int] (rotated)
          
          #PSDC: 
          #Enumerate list
          #while index is > k
              #push to new array 
              #enumerate again and push other half 
          
          k %= len(nums)
          nums[k:], nums[:k] = nums[:-k], nums[-k:]
          

4. CONTAINS DUPLICATE:

  def containsDuplicate(self, nums: List[int]) -> bool:
          # singles = []
          # dupes = [] 
          # for i in nums:
          #     if i not in singles:
          #         singles.append(i)
          #     else:
          #         dupes.append(i)
          # if len(dupes) > 0:
          #     return True
          # return False 
          
          return len(nums) > len(set(nums))
          

5. SINGLE NUMBER (Find the non duplicate number):
  class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupes = []
        for i in nums:
            if i not in dupes:
                dupes.append(i)
            else:
                dupes.remove(i)
        return dupes.pop()


6. PLUS ONE (Add one to the last int in list):
  class Solution:
      def plusOne(self, digits):
          
          # Edge case for single digit with 9 end
          if len(digits) == 1 and digits[0] == 9:
              return [1, 0]
          # Regular case to add one to last int
          if digits[-1] != 9:
              digits[-1] += 1
              return digits
          # Edge case for multi digit with 9 end
          else:
              digits[-1] = 0
              digits[:-1] = self.plusOne(digits[:-1])
              return digits  
        