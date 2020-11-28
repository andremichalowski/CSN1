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


-------------------------------------------

9 - CONDITIONALS AND BOOLEANS

x = 10
print(x == 10) # True
print(x == 5)  # False
print(x < 15)  # True
print(x > 15)  # False
print(x <= 10) # True
print(x >= 10) # True
print(x != 20) # True
You build up more complex boolean expressions by using the and and or operators.

name = "Elon"
age = 49
if name == "Elon" and age == 49:
    print("You are a 49 year old person named Elon.")

if name == "Elon" or name == "Bill":
    print("Your name is either Elon or Bill.")
Any time you have an iterable object (like a list), you can check if a specific item exists inside that iterable by using the in operator.

years = [2018, 2019, 2020, 2021]
year = 2020

if year in years:
    print("%s is in the years collection" % year)

# 2020 is in the years collection
We can use the if, elif, and the else keywords to define a series of code blocks that will execute conditionally.

first_statement = False
second_statement = True

if first_statement:
    print("The first statement is true")
elif second_statement:
    print("The second statement is true")
else:
    print("Neither the first statement nor the second statement are true")
Any object that is considered "empty" evaluates to False. For example, "", [], and 0 all evaluate to False.

If we want to determine if two objects are actually the same instance in memory, we use the is operator instead of the value comparison operator ==.

a = [1,2,3]
b = [1,2,3]

print(a == b) # True because a and b have the same value
print(a is b) # False because a and b reference two different list objects

x = [1,2,3]
y = x

print(x == y) # True because x and y have the same value
print(x is y) # True because x and y reference the same list object
There is also the not operator, which inverts the boolean that follows it:

print(not False)    # True
print(not (1 == 1)) # False because 1 == 1 is True and then is inverted by not


(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-conditional-expressions#main.py
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-conditional-expressions#main.py

!!! Return to revisit true statement \#2

----------------------------------------------

10 - LOOPS

Here is an example of a few different ways you can use a range as the iterable for a for loop.

# Prints 0, 1, 2, 3, 4
for x in range(5):
    print(x):

# Prints 2, 3, 4, 5, 6
for x in range(2, 7):
    print(x)

# Prints 1, 3, 5, 7
for x in range(1, 8, 2):
    print(x)
This example shows the simple usage of a while loop to print the same values as the for loops above.

# Prints 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count += 1

# Prints 2, 3, 4, 5, 6
count = 2
while count < 7:
    print(count)
    count += 1

# Prints 1, 3, 5, 7
count = 1
while count < 8:
    print(count)
      count += 2
You can use a break statement to exit a for loop or a while loop.

# Prints 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
You can also use a continue statement to skip the current block but not exit the loop entirely.

# Prints 1, 3, 5, 7
for x in range(8):
    # if x is even, skip this block and do not print
    if x % 2 == 0:
        continue
    print(x)

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-loops
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-loops#main.py

!!! Return to review other versions of loops / seek additional instruction

-------------------------------------------

11 - LIST COMPREHENSIONS

List comprehensions are a potent tool. With a list comprehension, you can create a new list based on another list in a single, highly readable line.

The format of a list comprehension follows this syntax:

[<map expression> for <name> in <sequence expression> if <filter expression>]

Follow Along
If you are using a for loop to map a list onto a new list or filter an existing list, a list comprehension can be a better option.

Here is an example of replacing a for loop used to map word lengths with a single line with a list comprehension.

sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = []

# Using a for loop
for word in words:
    word_lengths.append(len(word))

print(words)        # ['Every', 'moment', 'is', 'a', 'fresh', 'beginning.']
print(word_lengths) # [5, 6, 2, 1, 5, 10]

# Using a list comprehension
word_lengths = [len(word) for word in words]

print(word_lengths) # [5, 6, 2, 1, 5, 10]
Here is an example of replacing a for loop used to filter out odd numbers from a list with a list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

# Using a for loop
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers) # [2, 4, 6, 8, 10]

# Using a list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers) # [2, 4, 6, 8, 10]
You can also write a list comprehension that maps and filters simultaneously. Let's go back to our sentence example and only track word lengths that are greater than 2.

sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = []

# Using a for loop
for word in words:
    if len(word) > 2:
        word_lengths.append(len(word))

print(words)        # ['Every', 'moment', 'is', 'a', 'fresh', 'beginning.']
print(word_lengths) # [5, 6, 5, 10]

# Using a list comprehension
word_lengths = [len(word) for word in words if len(word) > 2]

print(word_lengths) # [5, 6, 5, 10]

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-list-comprehensions
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-list-comprehensions#main.py

---------------------------------------------------

12 - USER DEFINED FUNCTIONS


To define a function in Python, we follow this syntax:

def function_name(argument_1, argument_2, etc.):
    # function line 1
    # function line 2
    # etc.
Follow Along
Let's define a greeting function that allows us to specify a name and a specific greeting.

def greet(name, greeting):
    print("Hello, %s, %s" % (name, greeting))
Now, we can call our greet function and pass in the data that we want.

greet("Austen", "I hope you are having an excellent day!")
# Hello, Austen, I hope you are having an excellent day!
If we want to define a function that returns a value to the caller, we use the return keyword.

def double(x):
    return x * 2

eight = double(4)
print(eight)
# 8


(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-functions
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-functions#main.py

-----------------------------------------------

13 - Create user-defined classes and interact with instances of those classes

Let's define a class so we can use it as a blueprint for an object.

class MyFirstClass:
    variable = "data"

    def function(self):
        return "Printing from a MyFirstClass object."
Now, to create an object based on MyFirstClass, we call the class like a function and assign the instance object to a variable.

a_class_object = MyFirstClass()
Now we can use dot notation to access variables and functions on the object.

print(a_class_object.variable)
# data
print(a_class_object.function())
# Printing from a MyFirstClass object.

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-classes-and-instances
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-classes-and-instances#main.py

-----------------------------------------------

14 - DICTIONARIES

Let's use a dictionary to create a collection that maps first names as keys (strings) to phone numbers as values.

phonebook = {} # creates an empty dictionary
phonebook["Abe"] = 4569874321
phonebook["Bill"] = 7659803241
phonebook["Barry"] = 6573214789

print(phonebook)
# {'Abe': 4569874321, 'Bill': 7659803241, 'Barry': 6573214789}
Instead of adding one key-value pair at a time, we can initialize the dictionary to have the same values.

phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}

print(phonebook)
# {'Abe': 4569874321, 'Bill': 7659803241, 'Barry': 6573214789}
We can iterate over a dictionary as we iterated over a list. We can use the items() method, which returns a tuple with the key and value for each item in the dictionary.

for name, number in phonebook.items():
    print("Name: %s, Number: %s" % (name, number))

# Name: Abe, Number: 4569874321
# Name: Bill, Number: 7659803241
# Name: Barry, Number: 6573214789
To remove a key-value pair from a dictionary, you need to use the del keyword or use the pop() method available on dictionary objects. The difference is pop() deletes the item from the dictionary and returns the value. When you use the del keyword, you've written a statement that doesn't evaluate to anything.

phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}

del phonebook["Abe"]

print(phonebook.pop("Bill"))
# 7659803241

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-dictionaries
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-dictionaries#main.py

----------------------------------------------

15 - IMPORT MODULES

 Any Python file that ends with the .py extension is considered a module. The name of the module is the name of the file.

To import from other modules, we can use the import command.

import math

print(math.factorial(5))
# 120
So, by importing the built-in math module, we have access to all of the functions and data defined in that module. We access those functions and data using dot notation, just like we do with objects.

If you only need a specific function from a module, you can import that specific function like so:

from math import factorial

print(factorial(5))
# 120
You can also import all the names from a module with this syntax to avoid using dot notation throughout your file.

from math import *

print(factorial(5))
# 120
print(pow(2, 3))
# 8.0
You can also bind the module to a name of your choice by using as.

import math as alias

print(alias.factorial(5))
# 120
To find out which names a module defines when imported, you can use the dir() method. This method returns an alphabetically sorted list of strings for all of the names defined in the module.

import math

print(dir(math))
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

(REPLIT (CLEAN)) https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-1-modules
(REPLIT (DONE)) https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-1-modules#main.py

