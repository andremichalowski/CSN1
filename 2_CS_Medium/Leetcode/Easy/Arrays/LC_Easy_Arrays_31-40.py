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

6. "485 - MAX CONSECUTIVE ONES"

7. "495 - TEEMO ATTACKING"

8. "496 - NEXT GREATER ELEMENT"

9. "500 - KEYBOARD ROW"

10. "506 - RELATIVE RANKS"