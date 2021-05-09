1. Number of 1 Bits (HammingWeight):

  https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/

  # Easy way
  def hammingWeight(self, n: int) -> int:
          return bin(n).count('1')

  # Harder way - https://stackoverflow.com/questions/21237767/python-a-b-meaning
  def hammingWeight(self, n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c