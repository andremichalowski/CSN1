1. Logarithms:

  2^5 = 32
  2^0 = 1
  2^{-1} = \frac{1}{2}

  log_2 32 = 5
  log_2 1 = 0
  log_2 \frac{1}{2} = 1

2. WRITE A LINEAR SEARCH ALGORITHM:

  def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(len(arr)):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

    # REVERSE: for idx in reversed(range(len(arr))):

3. RECURSION:


def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum