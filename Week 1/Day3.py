*************** 1. Mutability ******************

Mutable Types	Immutable Types
list	                int
dictionary	          float
set	                  decimal
user-defined classes	bool
                      string
                      tuple
                      range




*************** 2. BIG O NOTATION ******************

Common Big O run times
Refer to the table below to see a list of the most common runtimes. The table is ordered from fastest to slowest.

Classification	Description
Constant    "O(1)":	      The runtime is entirely unaffected by the input size. This is the ideal solution.
Logarithmic "O(log n)":	  As the input size increases, the runtime will grow slightly slower. This is a pretty good solution.
Linear      "O(n)":	      As the input size increases, the runtime will grow at the same rate. This is a pretty good solution.
Polynomial  "O(n^c)":	    As the input size increases, the runtime will grow at a faster rate. This might work for small inputs but is not a scalable solution.
Exponential "O(c^n)":	    As the input size increases, the runtime will grow at a much faster rate. This solution is inefficient.
Factorial   "O(n!)":      As the input size increases, the runtime will grow astronomically, even with relatively small inputs. This solution is exceptionally inefficient.

(See graph for more detail: https://lambdaschool.instructure.com/courses/562/pages/objective-02-compare-the-time-complexity-of-different-approaches-to-a-problem-using-big-o-notation?module_item_id=527254)

1. Constant Time O(1)

  def print_only_one_thing(list_of_things):
      print(list_of_things[0])

  Why is this constant time? Because no matter how large or small the input is (1,000,000 or 10), the number of computations within the function is the same.


2. Linear Time O(n)

  def print_list(list_of_things):
      for thing in list_of_things:
          print(thing)

  Why is this classified as linear time? Because the speed of the algorithm increases at the same rate as the input size. If list_of_things has ten items, then the function will print ten times. If it has 10,000 items, then the function will print 10,000 times.


3. Quadratic Time O(n^2)

  def print_permutations(list_of_things):
      for thing_one in list_of_things:
          for thing_two in list_of_things:
              print(thing_one, thing_two)

  Why is this quadratic time? The clue is the nested for loops. These nested for loops mean that for each item in list_of_things (the outer loop), we iterate through every item in list_of_things (the inner loop). For an input size of n, we have to print n * n times or n^2 times.

REPLIT ... big o replit: https://repl.it/@AMichalowski/cs-unit-1-sprint-1-module-2-time-complexity#main.py




*************** 3. SPACE COMPLEXITY ******************

COMPLEXITY:
  SPACE - ANYTHING ADDITIONAL THE FUNCTION IS ADDING TO MEMORY #appending an item takes space
  TIME - NUMBER OF OPERATIONS #the more if else statemtns there are the more time it takes


replit: https://repl.it/@mdmccarley89/cs-unit-1-sprint-1-module-2-space-complexity#main.py


