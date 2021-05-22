OBJECTIVE 1: RECALL THE TIME AND SPACE COMPLEXITY, THE STRENGTHS AND WEAKNESSES, AND BASIC OPERATIONS OF A STATIC ARRAY:

Array Time complexity: O(1) (Insertions: O(n))

Array Space complexity: O(n)

Static Array Benefits and Weaknesses: O(1) to add to end or manipulate but O(n) to add to middle

OBJECTIVE 2: DESCRIBE DIFFERENCE BETWEEN IN PLACE AND OUT OF PLACE ALGORITHMS:

In place = edits over Array
  - less space
  - more prone to bugs
Out of place = edits new Array
  - more space
  - less prone to bugs

In place ex.:

  Here is an example of a function that triples each number in an input list. This function does this in-place:

  def append_exclamations(str_list):
      for idx, item in enumerate(str_list):
          str_list[idx] += "!"
  Now, since this is an in-place function, watch what happens when we use it:

  >>> my_list = ["Matt", "Beej", "Sean"]
  >>> append_exclamations(my_list)
  >>> my_list
  ['Matt!', 'Beej!', 'Sean!']

Out of place ex.:

  Let's now write a similar function, but this time we will do it out-of-place:

  def append_exclamations(str_list):
      # Create a new empty list that has the same length as the input list
      loud_list = [None] * len(str_list)
      for idx, item in enumerate(str_list):
          # insert the modified string into the new list
          loud_list[idx] = item + "!"
      # Since we didn't modify the input list, we need to return the new list to
      # the function caller
      return loud_list
  Look what happens when we use this function:

  >>> my_list = ["Matt", "Beej", "Sean"]
  >>> my_new_louder_list = append_exclamations(my_list)
  >>> my_list
  ['Matt', 'Beej', 'Sean']
  >>> my_new_louder_list
  ['Matt!', 'Beej!', 'Sean!']
  >>>


OBJECTIVE 3: RECALL THE TIME AND SPACE COMPLEXITY, THE STRENGTHS AND WEAKNESSES, AND BASIC OPERATIONS OF A DYNAMIC ARRAY

STATIC:
  TIME
  Lookup: O(1)
  Append: O(1) - O(n)
  Insert: O(n)
  Delete: O(n)

  SPACE: O(n)

DYNAMIC:
  Dynamic Arrays:
    - biggest strength is not having to know or worry about the size of the data structure.
    - weakness is that it creates a new array with whatever it cant fit

  TIME
  Lookup: O(1)
  Append: O(1) - O(n) (Because of doubling sometimes)
  Insertion: O(n)
  Deletion: O(n)

  SPACE: ? infinite O(n)?

