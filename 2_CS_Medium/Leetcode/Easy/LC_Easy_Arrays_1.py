from _typeshed import OpenBinaryMode


1. 1 - TWO SUM (Given an array ints and an int target: return indices of two numbers that add to target):
  class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i

2. 26 - REMOVE DUPLICATES FROM SORTED ARRAY (Given nums, remove duplicates (in place)):

  def removeDuplicates(self, nums: List[int]) -> int:
    index = 1
    while index < len(nums):
        if nums[index] == nums[index-1]: #check dup
            nums.pop(index)
        else:
            index += 1 #move cursor
    return len(nums)

3. 27 - REMOVE ELEMENT:

4. 35 - SEARCH INSERT POSITION:

5. 53 - MAXIMUM SUBARRAY:

6. 66 - PLUS ONE:

7. 88 - MERGE SORTED ARRAY:

8. 108 - CONVERT SORTED ARRAY TO BINARY SEARCH:

9. 118 - PASCALS TRIANGLE:

10. 119 - PASCALS TRAINGLE II: