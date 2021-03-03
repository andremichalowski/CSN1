1. MERGE SORTED ARRAY:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: #Number of elements initialized 9in nums1 and nums2 are m and n respectively.
          nums1[m:] = nums2[:n]
          nums1.sort()

2. 