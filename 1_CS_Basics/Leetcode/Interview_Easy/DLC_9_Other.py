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
            bit_str = '{0:032b}'.format(n) # Format n into bit string (length of 32)
            reverse_str = bit_str[::-1] # Reverse bit_string with slice fxnality
            return int(reverse_str, 2) # Return string as int w/ 2 
            
4. Pascals Triangle: 
    def generate(self, numRows):
        lists = []
        for i in range(numRows):
            lists.append([1]*(i+1))
            if i>1 :
                for j in range(1,i):
                    lists[i][j]=lists[i-1][j-1]+lists[i-1][j]
        return lists

5. Valid Parenthesis:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
    
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

6. Missing Number: (Missing number in an array)
    # One line
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

    # Two lines
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

        