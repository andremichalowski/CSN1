************************ DAY 1: ************************

# TK NOTES

--------------------------------------------------

1 - INSTALL PYTHON 
...

--------------------------------------------------

2 - PRINT STATEMENTS:

# Print with an expression
>>> superlative = "wonderful"
>>> school = "Lambda School"
>>> print(school + " is " + superlative)
Lambda School is wonderful
>>>

# Print with object types
print(2020)
2020
>>> print(123.456)
123.456
>>> print(False)
False
>>> print(["Lambda", "School", 2, 0, 2, 0])
['Lambda', 'School', 2, 0, 2, 0]
>>> print(("Lambda", "School"))
('Lambda', 'School')
>>> print({"school": "Lambda School", "year": 2020})
{'school': 'Lambda School', 'year': 2020}
>>>

# End statement
>>> print("Are you a Lambda School student?", end=" (Y or N)")
Are you a Lambda School student? (Y or N)>>>

# Sep statement
>>> print("Hello", "how are you?", sep="---")
Hello---how are you?

--------------------------------------------------

3 - WHITESPACE

#Whitespace Characters
Whitespace is any character represented by something that appears empty (usually \t or " "). The characters that Python considers to be whitespace can be seen by printing out the value of string.whitespace from the string library.

>>> import string
>>> string.whitespace
' \t\n\r\x0b\x0c'
>>>
Notice the characters are " " (space), \t (tab), \n (newline), \r (return), \x0b (unicode line tabulation), and \x0c (unicode form feed).

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-white-space#main.py
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-white-space-1#main.py


--------------------------------------------------

4 - BASIC TYPES (INTEGERS, FLOATS, STRINGS)

my_int = 2
my_float = 5.0
my_str = "Lambda School"

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-basic-types#main.py
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-basic-types#main.py

--------------------------------------------------

5 - BASIC LIST OPERATIONS

my_list = [] # empty list literal
my_list.append(1) # add 1 to end of list
my_list.append(2) # add 2 to end of list
my_list.append(3) # add 3 to end of list
print(my_list[0]) # prints 1
print(my_list[1]) # prints 2
print(my_list[2]) # prints 3

# iterate over the list with for statement to print each item in my_list
for item in my_list:
    print(item)

Last, let's iterate through our numbers list to sum up all of the numbers:

sum = 0
for number in numbers:
    sum += number

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-list-operations
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-list-operations#main.py


------------------------------------------------------

6 - BASIC OPERATORS

#Modulo
There is also an operator called the modulo operator (%). This operator returns the remainder of integer division.

my_remainder = 9 % 4
print(my_remainder) # 1

#Exponent
You can use two multiplication operators to make the exponentiation operator (**).

two_squared = 2 ** 2
print(two_squared)    # 4
two_cubed = 2 ** 3
print(two_cubed)      # 8


# Sample all

First, let's create two variables, a and b, where each variable stores an instance of the object class.

a = object()
b = object()
Next, let's see if we can make two lists, one containing five instances of a, and the second with five instances of b.

a_list = [a] * 5
b_list = [b] * 5
Then, let's combine a_list and b_list into a combined list.

combined = a_list + b_list
If our code works as expected, combined should have a length of 10.

print(len(combined)) # 10

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-basic-operators#main.py
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-basic-operators#main.py

----------------------------------------------

7 - Formatted STRINGS

#Sample 1 Formatted string
product_name = "bananas"
price = 1.23
product_id = 123456

We need to print a formatted string using argument specifiers and a tuple that contains our data:

print("%s (id: %d) are currently $%.2f." % (product_name, product_id, price))
# bananas (id: 123456) are currently $1.23.

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-formatted-strings
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-formatted-strings#main.py

------------------------------------------------

8 - STRING OPERATIONS

The len() method prints out the number of characters in the string.

my_string = "Hello, world!"
print(len(my_string)) # 12
The index() method prints out the index of the substring argument's first occurrence.

my_string = "Hello, world!"
print(my_string.index("o"))   # 4
print(my_string.index(", w")) # 5
The count() method returns the number of occurrences of the substring argument.

my_string = "Hello, world!"
print(my_string.count("o"))  # 2
print(my_string.count("ll")) # 1
To slice a string, you can use this syntax: [start:stop:step]. To reverse the string's order, you can set the step value to be -1.

my_string = "Hello, world!"
print(my_string[3:7])   # lo,
print(my_string[3:7:2]) # l,
print(my_string[::-1])  # !dlrow ,olleH
You can convert a string to uppercase or lowercase with the upper() and lower() methods.

my_string = "Hello, world!"
print(my_string.upper()) # HELLO, WORLD!
print(my_string.lower()) # hello, world!
You can determine if a string starts with or ends with a specific sequence with the startswith() and endswith() methods.

my_string = "Hello, world!"
print(my_string.startswith("Hello")) # True
print(my_string.endswith("globe!"))  # False
The split() method allows you to split up a string into a list. The default separator is any whitespace. You can also specify the separator value with an argument if you want.

my_string = "Hello, world!"
print(my_string.split())    # ['Hello,', 'world!']
print(my_string.split(",")) # ['Hello', ' world!']
print(my_string.split("l")) # ['He', '', 'o, wor', 'd!']

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-basic-string-operations
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-basic-string-operations#main.py


