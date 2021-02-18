1. WEAKNESS STATISTICS:
What are the two primary weaknesses of a static array as a data structure?
  1. Fixed Size
  2. O(n) insertions and deletions

2. PYTHON ARRAY SLICE:
What is the time and space complexity of slicing an array in Python?

  1. Time: O(n)
  2. Space: O(n)

3. OUT OF PLACE ALGORITHM:
Why are out-of-place algorithms generally considered to be safer?

  1. Because they avoid side-effects.

4. WORST CASE TIME 
In your own words, explain why the worst-case time cost of appending to a dynamic array is O(n).

  1. The worst case time cost of appending to a dynamic array is O(n) because if you append an item beyond the capacity of the array a new array (with a copy of the previous array) will be created to accommodate that item. This is called "doubling appends" and has a cost of O(n).

5. BUY AND SELL STOCK:
You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97


  def buyAndSellStock(prices):
      #INPUT: array of ints: 'prices'
      #OUTPUT: max profit (diff between max and min)
      
      # best_result = 0 
      # loop through all the numbers
          # loop again
      # difference between i and j
          # redefine best_result if best_result greater than new diff
      # return best_result
      
      # best_result = 0
      # for i in range(len(prices)-1):
      #     for j in range(i+1, len(prices)): 
      #         if prices[j] - prices[i] > best_result:
      #             best_result = prices[j] - prices[i]
      # return best_result
              
      max_profit = 0
      min_price_so_far = float('inf')
          
      for current_price in prices:
          min_price_so_far = min(current_price, min_price_so_far)
          best_possible_profit_if_sold_now = current_price - min_price_so_far
          max_profit = max(best_possible_profit_if_sold_now, max_profit)
          
      return max_profit

6. ALPHABETIC SHIFT:
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

  from string import ascii_lowercase

  def alphabeticShift(inputString):
      # print(ascii_lowercase)
      #INPUT: alpha string
      #OUTPUT: alpha string + 1
      
      #output string initialize
      #
      answer = ''
      strings  = ascii_lowercase+'a'
      for i in inputString:
          answer += strings[strings.index(i)+1]
      return answer

7. VALID PARENTHASESS:
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.

  def validParenthesesSequence(s):
    #STACK
    
    stack = [] 
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if popped != "(":
                return False
    if len(stack) > 0:
        return False
    return True
                