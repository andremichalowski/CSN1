1. Logarithms:

  2^5 = 32
  2^0 = 1
  2^{-1} = \frac{1}{2}

  log_2 32 = 5
  log_2 1 = 0
  log_2 \frac{1}{2} = 1

2. WRITE A LINEAR SEARCH ALGORITHM:

  def linear_search(arr, target):
    # loop through each item in the input array
    for idx in range(len(arr)):
        # check if the item at the current index is equal to the target
        if arr[idx] == target:
            # return the current index as the match
            return idx
    # if we were able to loop through the entire array, the target is not present
    return -1

    # REVERSE: for idx in reversed(range(len(arr))):

3. RECURSION (WHEN TO USE IT):

    3A. BASE EXAMPLES

    Sum list:

        def sum_list(items):
            if len(items) == 1:
                return items[0]
            else:
                return items[0] + sum_list(items[1:])

    Print to zero:

        def print_to_zero(n):
        print(n)
        if n == 0: # base case
            return
        return print_to_zero(n - 1) # recursive case

    
    3B. RULES OF RECURSION:
        1. Must have a base case
        2. Must change its state to move towards the base case
        3. Must call itself


    3C. WHERE YOU WOULD USE RECURSION:
        1. Compute the nth term
        2. List the first or last n terms
        3. Generate all permutations


    3D. COMPUTING FACTORIALS:
        def recursive_factorial(n):
            if n == 1:
                return 1
            else:
                return n * recursive_factorial(n - 1)

4. TRACE AND ACCURATELY IDENTIFY THE OUTPUT OF A RECURSIVE FUNCTION CALL:

    What is the call stack?
        The whole reason we are talking about stacks in the first place is so we can understand the call stack. Call stacks help us understand recursion.
        Whenever your program calls a function, the computer sets aside a chunk of memory for its execution context. Any variables in that function scope are stored here.
        The computer stores these chunks of memory in the call stack, which has two fundamental operations: pushing onto the top and popping off the stack's top.

    FIBONACCI SEQUENCE
        def recursive_fib(n):
            if n <= 1:
                return n
            else:
                n_minus_1 = recursive_fib(n-1)
                n_minus_2 = recursive_fib(n-2)
                return n_minus_1 + n_minus_2