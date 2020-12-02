4 steps in UPER problem solving framework?

  1. Understand, 2. Plan, 3. Execute, 4. Reflect

------------------------------------------

csUPERMostImportantActionInPlan

Most important part of plan step?

  Taking the problem and converting it into a complete actionable plan
  to solve that probelm

------------------------------------------

csRemoveTheVowels

Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

  def csRemoveTheVowels(input_str):
      
      vowels = "aeiouAEIOU"

      final_str = ''.join([ch for ch in input_str if ch not in vowels])
      
      print(final_str)
      
  #     vowels = "aeiouAEIOU"
  #     final_str = input_str
      
  #     for char in input_str:
  #         if char in vowels:
  #             output_str = final_str.replace(char, "")
              
  #     return final_str
  #     print(final_str)
              
  # print(csRemoveTheVowels("Lambda school is ok."))

------------------------------------------

csShortestWord

Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate 
for different data types.

  def csShortestWord(input_str):
    # Input: string of words
    # Output: length of shortest word
    
    #init shortest
    #split string to give you individual words
    #iterate over string (have to split because iterating the string would just give you letters?)
        # check for length of i
        # if i is shorter than shortest 
            # redefine shortest
    #return string
    
    shortest = ""
    split = input_str.split()
    for i in split:
        if len(shortest) == 0:
            continue
        if len(i) > shortest:
            shortest = i
    print(shortest)
        
    



------------------------------------------

csSumOfPositive

Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0

  def csSumOfPositive(input_arr):
    #INPUT: array of ints
    #OUTPUT: sum of all positive ints in array
    
    #init positives array
    #iterate array of ints
        #if int positive add to positives array
    #sum of positives
    
    positives = []
    for i in input_arr:
        if i > 0:
            positives.append(i)
        else:
            pass
    return sum(positives)


------------------------------------------

csLongestPossible

Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"

  def csLongestPossible(str_1, str_2):
  #input = strings
  #output = sorted string that contains one individual character that is contained in both original strings

  #make a sorted result string

  #push similar chars to sorted result string
      #filter one string for unique chars then push to 
      #filter second string for similar chars
    
    sorted_1 = []
    sorted_2 = []
    sorted_final = []

    #SORTING STR 1:
    for i in str_1:
        if sorted_1[len(sorted_1) - 1] == i:
            pass
        elif sorted_1[len(sorted_1) - 1] != i:
            sorted_1.append(i)

    #SORTING STR 2:
    for i in str_2:
        if sorted_2[len(sorted_2) - 1] == i:
            pass
        elif sorted_2[len(sorted_2) - 1] != i:
            sorted_2.append(i)   

    #SORTING FROM BOTH STRINGS
    for i in sorted_1:
        if sorted_final[len(sorted_final) - 1] == i:
            pass
        elif sorted_final[len(sorted_final) - 1] != i:
            sorted_final.append(i)
            for j in sorted_2:
                if sorted_final[len(sorted_final) - 1] == j:
                    pass
                elif sorted_final[len(sorted_final) - 1] != j:
                    sorted_final.append(j)

    return sorted_final
        

   


------------------------------------------

csAnythingButFive

Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12

  def csAnythingButFive(start, end):
    #INPUT: Start int and end int
    #OUTPUT: Count except 5 in that range
    
    #Init 'but_five'
    #Create a range from 'start' to 'end'
    #Iterate range
        #If i != 5: continue
        #elif i = 5: pass
    #
    
    but_five = []
    for i in range(start, end):
        for j in range(start, end, 5):
            if i != j:
                but_five.append(i)
            else:
                continue
    return len(but_five)
    
  # print(csAnythingButFive(4, 10))
  #elif but_five[len(but_five)-1].contains(5):
  #elif 4 in but_five[len(but_five)-1]:
  # 
  # if i != 5:
  #             but_five.append(i)
  #         elif i == 5 or i == 15 or i == 25 or i == 35 or i == 45 or i == 55 or i == 65:
  #             continue


------------------------------------------

