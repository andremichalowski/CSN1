1. TIME COMPLEXITY HASH OPERATIONS:
  What is the average time complexity of the following operations on a hash table:
    - lookup, insert, delete

  # O(n)
  # O(log n)
  # O(2n)
  >>>> O(1)


2. PRIMARY WEAKNESS OF HASH TABLES:
  What are the primary weaknesses of a hash table?

  >>>> If you have the key, you can quickly retrieve the value. However, if you have the value and need to get the keys, that is a slow O(n) operation.
  >>>> In the worst case, all operations have an O(n) time complexity.
  >>>> The keys are not stored in any order.
  # They are not that flexible because you can only use integers as keys.


3. COMMON STRATEGY FOR COLLISIONS:
  What is the most common strategy for dealing with hash collisions?

  >>>> Not storing the values directly at an index of the hash table\'s array. Instead the array index stores a pointer to a linked list. Each node in the linked list stores a key, value, and a pointer to the next item in the linked list. 


4. FIND THE SINGLE NUMBER:
  You are given a non-empty array of integers.
  One element appears exactly once, with every other element appearing at least twice, perhaps more.
  Write a function that can find and return the element that appears exactly once.

  from collections import defaultdict

  def csFindTheSingleNumber(nums):
      hash_table = defaultdict(int)
      for i in nums:
          hash_table[i] += 1
      
      for i in hash_table:
          if hash_table[i] == 1:
              return i

5. AVERAGE OF TOP FIVE:

  Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

  Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

  Example 1:

  Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
  Output: [[1,87],[2,88]]
  Explanation:
  The average student `1` is `87`.
  The average of student `2` is `88.6`, but with integer division is `88`.


  import math

  def csAverageOfTopFive(scores):

      students = {}
      ans = []
      count = 0
      if scores is None:
          return scores
      for score in scores:
          if score[0] not in students:
              students[score[0]] = []
          students[score[0]].append(score[1])
      for student in students:
          student = students[student].sort()
      for s in students: 
          if len(students[s]) > 5:
              students[s] = students[s][-5:]
      for k in students:     
          students[k] = math.floor(sum(students[k]) / len(students[k]))  
      for key, val in students.items():
          ans.append([key,val])
      return ans



6. MAX NUMBER OF LAMBDAS:

  Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

  You can use each character in text at most once.

  Write a function that returns the maximum number of instances of "lambda" that can be formed.

  Example 1:

  Input: text = "mbxcdatlas"
  Output: 1


  def csMaxNumberOfLambdas(text):
      letters_dict = { "l": 0, "m": 0, "b": 0, "d": 0, "a": 0 }
      for letter in text:
          if letter in letters_dict:
              letters_dict[letter] += 1
      letters_dict['a'] = letters_dict['a'] / 2
      return min(letters_dict.values())

    

  from collections import Counter
  def csMaxNumberOfLambdas(text):
      cnt = 0
      c1 = Counter(text) 
      c2 = Counter('lambda')
      c1.subtract(c2)
      while all([elem >= 0 for elem in c1.values()]):
          cnt += 1
          c1.subtract(c2)
      return cnt