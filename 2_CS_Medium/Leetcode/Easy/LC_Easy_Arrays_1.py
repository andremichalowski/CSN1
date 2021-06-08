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

3. 27 - REMOVE ELEMENT (Given nums and val remove all instance of val in nums (in place)):

  def removeElement(self, nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

4. 35 - SEARCH INSERT POSITION (Given sorted arr and val, return index of val if found : index where it would be):

  def searchInsert(self, nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)

5. 53 - MAXIMUM SUBARRAY (Find max subarray in nums and return its sum):

  def maxSubArray(self, nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

    # If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
    # If the sum is negative, it has no use to the next element, so we break.
    # it is a game of sum, not the elements.
  
6. 66 - PLUS ONE:

7. 88 - MERGE SORTED ARRAY:

8. 108 - CONVERT SORTED ARRAY TO BINARY SEARCH:

9. 118 - PASCALS TRIANGLE:

10. 119 - PASCALS TRAINGLE II: