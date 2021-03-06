1. MERGE SORTED ARRAY:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: #Number of elements initialized 9in nums1 and nums2 are m and n respectively.
          nums1[m:] = nums2[:n]
          nums1.sort()

2. FIRST BAD VERSION:

Iterative Version:
  def firstBadVersion(self, n):
        low = 1
        high = n
        while(low < high):
            mid = (low + high)/2
            if isBadVersion(mid) == True:
                high = mid
            else:
                low = mid + 1
        return int(high)

Recursive Version:
  def firstBadVersion(self, n):
      return self.binarySearch(1, n)
  
  def binarySearch(self, low, high):
      if low == high:
          return low
      mid = (low + high)/2
      if isBadVersion(mid) == True:
          return self.binarySearch(low, mid)
      else:
          return self.binarySearch(mid + 1, high)