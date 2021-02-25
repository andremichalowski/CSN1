1. CSLOGARITHMICEXPRESSION:

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