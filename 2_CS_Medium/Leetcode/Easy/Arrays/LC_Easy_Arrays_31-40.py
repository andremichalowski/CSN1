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

4. "455 - ASSIGN COOKIES"

5. "463 - ISLAND PERIMETER"

6. "485 - MAX CONSECUTIVE ONES"

7. "495 - TEEMO ATTACKING"

8. "496 - NEXT GREATER ELEMENT"

9. "500 - KEYBOARD ROW"

10. "506 - RELATIVE RANKS"