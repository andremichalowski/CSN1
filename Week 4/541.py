1. HASH TABLES INTRO:

  TC: (BEST CASE/WORST CASE) = O(1) / O(n)
  SC: O(n)

  Strengths: 
    O(1) average lookup etc. 
    Can use any hashable object as key

  Weakness:
    mapping goes one way so unless you know the key its going to be innefficient to find the value


2. DESCRIBE AND IMPLEMENT A HASH FUNCTION:

  def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size


3. 