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

2. Hamming Distance:

    # Easy Way
    bin(x ^ y).count('1')

    #Right way (Bitwise Operators): https://code.tutsplus.com/articles/understanding-bitwise-operators--active-11301
    
    # Approach 1: Just check every bit in both numbers and increment when they are different
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                hamming_distance += 1
            x = x >> 1
            y = y >> 1
        return hamming_distance

    # Approach 2: Just make XOR of x and y and after that count the number of '1' bits.
    # because XOR of two different bits is always 1
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        new = x ^ y
        while new > 0:
            if new % 2 == 1:
                hamming_distance += 1
            new = new >> 1
        return hamming_distance

    # Approach 3: Again make XOR of x and y but when we count the number of '1' bits
    # we make the trick n&(n-1) which removes last '1' bit
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        new = x ^ y
        while new > 0:
            new = new & (new-1)
            hamming_distance += 1
        return hamming_distance

    # Good explanation of XOR solution: https://www.youtube.com/watch?v=UP4GhCxeC4I

3. Reverse Bits (Reverse Bits of a 32 bits unsigned integer):

    # https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/648/discuss/54932/Three-different-solutions-in-python
    def reverseBits(self, n):
            bit_str = '{0:032b}'.format(n) # Format n into bit string
            reverse_str = bit_str[::-1] # Reverse bit_string with slice fxnality
            return int(reverse_str, 2) # Return string as int w/ 2 
            
    
