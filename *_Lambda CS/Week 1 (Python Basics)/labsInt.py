# Find all the pairs of two integers in an unsorted array that sum up 
# to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and
#  the sum is 7, your program should return [[11, -4], [2, 5]]  11 + -4 = 7 and 2 + 5 = 7

# INPUT: An array (list)
# OUTPUT: All pairs that sum a given #S (integer)

def twoSum(givenA, s: int) -> int:
  if array == []:
    return -1
  # store array

  # iterating over the array
    # iterate over the array again 
      # if i + s == s:
        # arr.append([i, j])

  # return arr

  arr = []

  for i in givenA:
    for j in givenA: # range(len(s))
      if i + j == s:
        arr.append([i, j])

  return arr