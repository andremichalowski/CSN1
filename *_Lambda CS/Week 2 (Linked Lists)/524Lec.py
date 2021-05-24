Sean Chen Dec 10th - SEARCHING AND RECURSION: https://youtu.be/gCBcfo4SDI4

1. ITERATIVE SEARCH IMPLEMENTATION WITH A RECURSIVE SEARCH IMPLEMENTATION:

  1. ITERATIVE SEARCH:

  def iter_search(arr, tar)
    for i, thing in enumerate(arr):
      if thing == target:
        return i
    return -1

  2. RECURSIVE SEARCH:

    def rec_search(arr, target):
      if len(arr) == 0:
        return -1
      if arr[-1] == target:
        return len(arr) -1
      return rec_search(arr.pop(), target)


2. RECURSIVE BINARY SEARCH:

  def binary_search(arr, target, left, right):
    if left <= right:
        midpoint = (right + left) // 2
        if arr[midpoint] == target:
            return midpoint 
        if arr[midpoint] < target:
            return binary_search(arr, target, midpoint + 1, right)
        else:
            return binary_search(arr, target, left, midpoint - 1)
    return -1   


3. FIND ROTATION POINT (Started somewhere in phonebook and then doubled back to start):

  def find_rotation_point(surnames):
    left = 0
    right = len(surnames) - 1
    while left < right:
        midpoint = (left + right) // 2
        if surnames[midpoint] > surnames[0]:
            left = midpoint
        else:
            right = midpoint 
        if left + 1 == right:
            return right 