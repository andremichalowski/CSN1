1. CSTIMECOMPLEXITY:

Using Big O notation, what is the correct classifcation of time complexity for the function below?

def do_lots_of_things(items):
  last = len(items) - 1
  print(items[last])

  middle = len(items) / 2
  i = 0
  while i < middle:
    print(items[i])
    i += 1
  for num in range(100):
    print(num)

>>>> O(n)    #not O(log n) or O(n^2) or O(1)
-----------------------------------------------

2. csSpaceComplexity:

Using Big O notation, what is the correct classifcation of time complexity for the function below?

def do_a_couple_things(n):
  my_list = []
  my_second_list = [0] * 26

  for _ in range(n):
    my_list.append("lambda")
    print(my_second_list[n % 25])
  
  return my_list
  
  O(n)       #not O(log n) or O(n^2) or O(1)

-----------------------------------------------
  

3. CCSORTED TWO SUM

Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.

def csSortedTwoSum(numbers, target):
     #INPUT: Array of ints (ascending), target int
     #OUTPUT: 2 ints whose sum = target int
     
     #Find two ints that add up to target
     #loop for ints
        #second loop for ints 
            # if I + J = target
            #return [i, j]
    
    # """
    # :type nums: List[int]
    # :type target: int
    # :rtype: List[int]
    # """
    index_map = {}
    for i in range(len(numbers)):
        num = numbers[i]
        pair = target - num
        if pair in index_map:
            return [index_map[pair], i]
        index_map[num] = i
    return None
    
    https://yuhongjun.github.io/tech/2017/06/14/(LeetCode-167-Easy)Two-Sum-II-Input-array-is-sorted.html
    # for i in numbers:
    #     for j in numbers:
    #         if i + j == target:
    #             return [i, j]
    #         else:
    #             continue   

# print(csSortedTwoSum([1,2,3,4,5], 9)

-----------------------------------------------

4. FIND ADDED LETTER

You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
csFindAddedLetter(str_1 = "bf", str_2 = "bfb") -> "b"
Notes:

str_1 and str_2 both consist of only lowercase alpha characters.

def csFindAddedLetter(str_1, str_2):
    #INPUT: string 1, string_1 scrambled + a letter
    #OUTPUT: letter added to string 1
                
    # for i in str_1:
    #     for j in str_2:
    #         if j not in str_2:
    #             return j

    # str_2.split().sort().join()
    
    # for i in str_1:
    #     for j in str_2:
    #        print(i + j)
    
    # for j in str_2:
    #     return str_2[(len(str_2)-1)]
    
    # for i in str_1:
    #     for j in str_2:
    #         if j not in str_1:
    #             return j
    
    #sort str_1
    # chars_1 = [char for char in str_1]
    # chars1sorted = chars_1.sort()
    #
    # chars_2 = [char for char in str_2]
    # chars1sorted = chars_2.sort()
    #
    # return chars_1
    
    
    # for i in str_2:
    #     if i != (for i in str_1):
    #         return i
            
    
     
    str1_lets = [chars for chars in str_1]
    str2_lets = [chars for chars in str_2]
   
    for i in range(len(str_1)):
        for j in range(len(str_2)):
            for k in str_2:
                if str_1[i] == str_2[j] or str_1 == "":
                    return str_2[(len(str_2)-1)]
                #...
                elif str2_lets[i] == str1_lets[i]:
                    continue
                elif str2_lets[i] != str1_lets[i]:
                    return str2_lets[i]
                elif str2_lets[j] != str1_lets[i]:
                    return str2_lets[j]
                else:
                    return "Problems!"

-----------------------------------------------

5. FIRST UNIQUE CHARACTER:

Given a string, write a function that returns the index of the first unique (non-repeating) character. 
If there isn\'t a unique (non-repeating) character, return -1.

def csFirstUniqueChar(s):
    #INPUT: string
    #OUTPUT: first unique (non-repeating) character
    
    if s == '':
        return -1

    for item in s:
        if s.count(item) == 1:
            return s.index(item)
            break

    return -1