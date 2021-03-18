1. REMOVE DUPLICATES:
    def removeDuplicates(self, nums):
            len_ = 1
            if len(nums)==0:
                return 0
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]:
                    nums[len_] = nums[i]
                    len_ +=1
            return len_


2. BEST TIME TO BUY AND SELL STOCK:
    def maxProfit(self, prices: List[int]) -> int:
            profit = 0
            for i in range(1, len(prices)):
                profit += max(prices[i]-prices[i-1], 0)
            return profit


3. ROTATE ARRAY:
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
          

5. SINGLE NUMBER: (Find the non duplicate number):
    def singleNumber(self, nums: List[int]) -> int:
        dupes = []
        for i in nums:
            if i not in dupes:
                dupes.append(i)
            else:
                dupes.remove(i)
        return dupes.pop()


6. PLUS ONE:¡ (Add one to the last int in list):
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
        

7. INTERSECTION OF TWO ARRAYS:      

(Daily Leetcode January 9th)

Two pointers:
    class Solution(object):
        def intersect(self, nums1, nums2):

            nums1, nums2 = sorted(nums1), sorted(nums2)
            pt1 = pt2 = 0
            res = []

            while True:
                try:
                    if nums1[pt1] > nums2[pt2]:
                        pt2 += 1
                    elif nums1[pt1] < nums2[pt2]:
                        pt1 += 1
                    else:
                        res.append(nums1[pt1])
                        pt1 += 1
                        pt2 += 1
                except IndexError:
                    break

            return res


Use dictionary to count:
    class Solution(object):
        def intersect(self, nums1, nums2):

            counts = {}
            res = []

            for num in nums1:
                counts[num] = counts.get(num, 0) + 1

            for num in nums2:
                if num in counts and counts[num] > 0:
                    res.append(num)
                    counts[num] -= 1

            return res


Use Counter to make it cleaner:
    class Solution(object):
        def intersect(self, nums1, nums2):

            counts = collections.Counter(nums1)
            res = []

            for num in nums2:
                if counts[num] > 0:
                    res += num,
                    counts[num] -= 1

            return res


8. MOVE ZEROES:

    # class Solution:
    #     def moveZeroes(self, nums: List[int]) -> None:
    #         """
    #         Do not return anything, modify nums in-place instead.
    #         """
    #         for i in range(len(nums)):
    #             if nums[i] == 0:
    #                 zero = nums.pop(i)
    #                 nums.append(zero)
    #             else:
    #                 continue

    # for i in range(len(nums)):
            # if nums[i] == 0:
            #     nums.remove(nums[i])
            #     nums.append(0)
            # else:
            #     continue
            # return nums
    # in-place
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

9. TWO SUM: (Sum of two nums in array = target):

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i