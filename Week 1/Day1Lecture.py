Python 511 w/TOM TARPEY: https://www.youtube.com/watch?v=doyxR2QByWY

+ Sean Chen?

1. ADDITION:

def addition(a, b):
    return a + b

2. TIME CONVERSION:

def convert(minutes):
    return minutes*60

3. STRING TO INT:

def string_int(txtdd):
    # Your code here
    return int(txt)

4. PARAMATERS FOR PERIMETER:

def find_perimeter(length, width):
    # Your code here
    return (length + width) * 2

5. SORT STRINGS BY ASCENDING ORDER:

def sort_by_length(lst):
    lst.sort(key=lambda x: (len(x), x))
    return lst

6. CHECKS TO SEE IF SAME NUMBER OF CHARACTER X VS O:

def XO(txt):
    num_xs = 0
    num_os = 0

    for letter in txt.lower():
        if letter == 'x':
            num_xs += 1
        if letter == 'o':
            num_os += 1
​
    return num_xs == num_os

7. RETURN THE NTH SMALLEST NUMBER:

def nth_smallest(lst, n):
    if n <= len(lst) and n > 0: #check for out of range
        lst.sort()
        return lst[n-1]

    return None

8. RETURN THE NUMBER OF ARGUEMENTS (LENGTH OF ITEMS IN PARAM):

def num_args(*args)
  return len(args)

9. CREATE DICTIONARY WITH UPPERCASE LETTER FOR EACH LOWERCASE:

def mapping(letters):
    # Your code here
​
    # we can write this tersely with a dictionary comprehension
    # return {letter: letter.upper() for letter in letters}
​
    # more explicitly
    d = {}
​
    for letter in letters:
        # set the key as the lowercase letter and the value
        # as the same letter uppercased 
        d[letter] = letter.upper()
​
    return d

10. CREATE A FXN THAT APPLIES DISCOUNT TO EVERY NUM IN LIST:

#EX: - get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]

def get_discounts(nums, percentage):

    discount = int(percentage[:-1]) / 100

    discounted = []
​
    for n in nums:
        discounted.append(n * discount)
​
    return discounted