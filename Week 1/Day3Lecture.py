Sean Chen: https://youtu.be/WJCbOczF14w

1. TWO SUM PROBLEM:

def two_sum(nums, target):
    d = {}
    for index, num in enumerate(nums): # O(n)
        d[num] = index 
    for index, num in enumerate(nums): # O(n)
        diff = target - num 
        if diff in d: # O(1)
			if diff == num:
            	return [index, d[diff]]
    return [-1, -1]
print(two_sum([2,5,9,13], 18))


2. SINGLE NUM PROBLEM:

def single_number(nums):
    s = set()
    for num in nums:
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    return s.pop()