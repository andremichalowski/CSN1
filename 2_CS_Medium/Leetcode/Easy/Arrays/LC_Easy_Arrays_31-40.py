1. "422 - VALID WORD SQUARE Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums."

(See https://www.youtube.com/watch?v=xJl_PE0Wu14)

2. "448 - FIND ALL NUMBERS DISSAPPEARING"

  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1
    
    res = []
    for i,n in enumerate(nums):
        if n > 0:
            res.append(i+1)
      
    return res

    
3. "453 - MINIMUM MOVES TO EQUAL (Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.)"

    def minMoves(self, nums):
        nums.sort()
        c = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            c += nums[i] - nums[0]
        return c

4. "455 - ASSIGN COOKIES Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number."

    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        childi = 0
        cookiei = 0
        
        while cookiei < len(s) and childi < len(g):
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1
        
        return childi

5. "463 - ISLAND PERIMETER You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island."

    def islandPerimeter(self, grid):
        if not grid:
            return 0

        def sum_adjacent(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count

6. "485 - MAX CONSECUTIVE ONES: Given a binary array nums, return the maximum number of consecutive 1's in the array."

    def findMaxConsecutiveOnes(self, nums):
        cnt = 0 # Create counter variable
        ans = 0 # Create answer variable
        for num in nums: # Loop through nums
            if num == 1: # If num is one
                cnt += 1 # Increment counter
                ans = max(ans, cnt) # Compare to ans and update if max
            else:
                cnt = 0 # Reset counter when reaches 0 or end
        return ans # return answer 

7. "495 - TEEMO ATTACKING" # Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack. # You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration. # Return the total number of seconds that Ashe is poisoned.

    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries) # ans var = duration * length of the time series
        for i in range(1,len(timeSeries)): # loop through length of time series
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1])) # ans decrement the difference between duration and (difference between time series sections)
        return ans

8. "496 - NEXT GREATER ELEMENT" # The next greater element of some element x in an array is the first greater element that is to the right of x in the same array. # You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. # For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. # Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

    def nextGreaterElement(findNums, nums):
        d = {}
        st = []
        ans = []
        
        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in findNums:
            ans.append(d.get(x, -1))
            
        return ans

9. "500 - KEYBOARD ROW"

10. "506 - RELATIVE RANKS"