21. 228 - SUMMARY RANGES (Find the smallest set of ranges that summarize the ints in arr):

  # Collect the ranges then format and return them
  def summaryRanges(self, nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

  # w/extra variable
  def summaryRanges(self, nums):
    ranges, r = [], []
    for n in nums:
        if n-1 not in r:
            r = []
            ranges += r,
        r[1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

22. 243 - SHORTEST WORD DISTANCE:

23. 252 - MEETING ROOMS:

24. 268 - MISSING NUMBER:

25. 283 - MOVE ZEROES:

26. 303 - RANGE SUM QUERY IMMUTABLE:

27. 346 - MOVING AVERAGE FROM DATA STREAM:

28. 350 - INTERSECTION OF TWO ARRAYS:

29. 414 - THIRD MAXIMUM NUMBER:

30. 422 - VALID WORD SQUARE: