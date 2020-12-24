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


Let's start writing out our function in pseudocode:

sum_list(items)
    if the length of items is one
        return the one item in the list
But what if someone asks us to sum more than one item? We must sum the first number and the sum of the rest of the items in the list.

Let's add this to our pseudocode:

sum_list(items)
    if the length of items is one
        return the one item in the list
    otherwise
        return the first item from the list + sum_list(the rest of the items)
Now let's convert our pseudocode into actual Python code:

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])