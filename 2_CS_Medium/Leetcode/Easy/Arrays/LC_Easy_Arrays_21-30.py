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

22. 243 - SHORTEST WORD DISTANCE (Find the shortest distance between two words in an arr of strs):

  def shortestDistance(self, words, word1, word2):
    dist = float("inf")
    i, index1, index2 = 0, None, None
    while i < len(words):
        if words[i] == word1:
            index1 = i
        elif words[i] == word2:
            index2 = i

        if index1 is not None and index2 is not None:
            dist = min(dist, abs(index1 - index2))
        i += 1
 