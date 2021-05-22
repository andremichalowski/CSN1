1. PIVOT INDEX: SUM NUMS ON LEFT = SUM NUMS ON RIGHT:

def pivot_index(nums):
    total = sum(nums) # O(n)
    running = 0 
    for i, num in enumerate(nums):
        total -= num
        if total == running:
            return i
        running += num
    return -1
​
nums = [1,2,3]
print(pivot_index(nums))


2. PLUS ONE:

"""
Example 1:
​
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
​
Example 2:
​
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
​
Example 3:
​
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""

"""
Here's the code we wrote for the plus_one problem.
To explain a bit more why the digits.insert() call is O(n) time, this how to do with how lists are laid out in memory. For example, if we have a list such as [3, 1, 2] and we want to insert a 4 at the beginning of this list to get [4, 3, 1, 2], how is that done under the hood?
Because of the fact that we expect that the inserted 4 will be at index 0 after the insertion, this means that the 3 has to be moved to index 1, the 1 has to be moved to index 2, and the 2 has to be moved to index 3. This all has to happen so that the slot at index 0 is available for us to park the 4 there.
To illustrate this, here's the starting state of our list, with indices to denote where each element is:
  0  1  2  
[ 3, 1, 2]
Again, we need to make space for the 4 at index 0, so in order to do that, our list is updated so that it looks like this (where the _ is denoting where the 4 will go):
  0  1  2  3
[ _, 3, 1, 2 ]
Now there's space for us to park the 4 at index 0, so we end up with the final state of our list:
  0  1  2  3
[ 4, 3, 1, 2 ]
The TL;DR here is that, when adding an element anywhere except the back of the list (using append / push methods), the runtime for such an operation is worst case O(n), due to the fact that we need to shift every element after the spot we want to insert into over by 1 spot. This is necessary because we have to make room for the new element we want to insert.
"""



def plus_one(digits):

​
    # iterate in reverse 
    for i in range(len(digits)-1, -1, -1):
        # check if the current digit == 9 
        if digits[i] != 9:
            digits[i] += 1
            # we're done; return our result 
            return digits
​
        # otherwise, the current digit is 9 
        digits[i] = 0 
        
    # if we reach outside of this for loop, then we got nothing but 9's 
    # we need to add a 1 to the front of our list 
    # Can be O(n) space in rare cases, but generally doesn't happen enough for us 
    # to consider it 
    # It is O(n) time complexity 
    digits.insert(0, 1) 
​
    return digits
​
print(plus_one([9,9])