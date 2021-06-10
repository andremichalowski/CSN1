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
  
6. 66 - PLUS ONE (Convert list of ints into a single int comprised of those ints in order):

  def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

  # We're given a list of digits, and the idea here is to convert that list to an integer, num. So each digit is multiplied by the proper place value and added to num. For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on.
  # The last step is to add 1 to num, convert it to a list and return that list.

7. 88 - MERGE SORTED ARRAY (Merge two arrays and sort them. Ignore zeros):

  def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]

8. 108 - CONVERT SORTED ARRAY TO BINARY SEARCH:

9. 118 - PASCALS TRIANGLE:

10. 119 - PASCALS TRAINGLE II: