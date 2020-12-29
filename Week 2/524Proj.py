51. CSLOGARITHMICEXPRESSION:

  Which logarithmic expresison is identical to the following exponential expression?
    2^n = 64 >>> n = log_2 64


2. LOGARITHM KEYWORDS:

  Keywords that show logarithms are involved?

  binary search + divide in half <<<

  ???(height of tree, selection sort, divide in half, double, linear search, none of above)


3. SELECTSEARCHING ALGORITHM:

  What type of search algorithm is used in this representation? (Displays a binary search)

  >>>Binary search


4. BINARY SEARCH ALGORITHM:

  def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    while first <= last:
      mid = first + (last - first) // 2
      if item_list[mid] == item:
        return True
      else:
        if item < item_list[mid]:
          last = mid - 1
        else:
          first = mid + 1
    return False

    What must be true for this algorithm to work?


5. FIBONACCI SIMPLE SUM:

  For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

  def fibonacciSimpleSum2(number):
    if number < 12:
        return True

    numbers = {0, 1, 2, 3, 5}

    last_number = 5
    this_number = 8

    while this_number <= number:

        numbers.add(this_number)
        target = number - this_number

        if target in numbers or target == this_number:
            return True
        
        next_number = last_number + this_number
        last_number = this_number
        this_number = next_number
    return False


6. BINARY SEARCH:

  Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

  def csBinarySearch(nums, target):
    # I:  nums = sorted(asc) integer array
    #     target = integer value desired
    # O:  Exists: return Index
    #     !Exist: return -1
    
    # If number e
        
    # min = 0
    # max = len(nums) - 1
    # while min < max:
    #     mid_guess = (max + min) // 2
    #     if nums[mid_guess] == target:
    #         return mid_guess
    #     elif nums[mid_guess] < target:
    #         min = mid_guess + 1
    #     elif nums[mid_guess] < target:
    #         min = mid_guess + 1
    #     else:
    #         max = mid_guess - 1
    # return -1
        
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


7. SEARCH ROTATED SORTED ARRAY:

  def csSearchRotatedSortedArray(nums, target):
      
      # left = 0
      # right = len(nums) - 1
      # while left < right:
      #     midpoint = (left + right) // 2
      #     if nums[midpoint] > nums[0]:
      #         left = midpoint
      #     else:
      #         right = midpoint 
      #     if left + 1 == right:
      #         return right 

      i = 0
      n = len(nums)
      while i < n and nums[i] != target:
          i += 1
      if i < n:
          return i
      return -1