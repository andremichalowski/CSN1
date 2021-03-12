1. DIY HT (REVISITED?):

  """
  Your task is create your own HashTable without using a built-in library.
  ​
  Your HashTable needs to have the following functions:
  ​
  - put(key, value) : Inserts a (key, value) pair into the HashTable. If the
  value already exists in the HashTable, update the value.
  - get(key): Returns the value to which the specified key is mapped, or -1 if
  this map contains no mapping for the key.
  - remove(key) : Remove the mapping for the value key if this map contains the
  mapping for the key.
  ​
  Example:
  ​
  ```plaintext
  hash_table = MyHashTable();
  hash_table.put("a", 1);
  hash_table.put("b", 2);
  hash_table.get("a");            // returns 1
  hash_table.get("c");            // returns -1 (not found)
  hash_table.put("b", 1);         // update the existing value
  hash_table.get("b");            // returns 1
  hash_table.remove("b");         // remove the mapping for 2
  hash_table.get("b");            // returns -1 (not found)
  ```
  """
  # O(1)
  def hash_fn(key, length):
      return id(key) % length
  ​
  # Linked list so that we can implement linked list chaining 
  class ListNode:
      def __init__(self, key, value):
          self.key = key 
          self.value = value 
          self.next = None
  ​
  class MyHashTable:
      def __init__(self, capacity, hash_fn=hash_fn):
          # Your code here
          # init our storage with some positive number of empty slots 
          self.storage = [None] * capacity
          # Some function that takes a key and spits out an integer 
          # we can make sure that the output is in bounds of our storage
          # by using % 
          self.hash_fn = hash_fn
  ​
      def print_storage(self):
          print(self.storage)
  ​
      '''
      Add the key and value as a pair in the hash table. 
      If the value already exists in the HashTable, update the value.
      '''
      def put(self, key, value):
          # Your code here
          # 1. Run the key through our hash function 
          # 2. set storage[index] = (key, value)
          # This will have the effect of updating a key that already existed 
          # in our hash table 
          # Doesn't handle collisions at all 
          index = self.hash_fn(key, len(self.storage))
  ​
          # check if this index is taken 
              # if it is taken, check the incoming key against the current key 
              # if they match, overwrite 
              # if they don't, still overwrite, but also print a message saying
              # we're overwriting 
          if self.storage[index] is not None:
              # we are inserting a key that already exists 
              # we want to overwrite the key's value 
              # but it isn't enough to just check the first linked list node 
              # at this index; we need to traverse the linked list
              current = self.storage[index]
  ​
              while current is not None:
                  if current.key != key:
                      current = current.next
                  else:
                      # we found the key whose value we want to overwrite 
                      current.value = value
                      break
  ​
                  if current.next is None:
                      # if we reach the end of the while loop, then we didn't end up
                      # overwriting a value; instead we need to add a new node to
                      # the end of the linked list 
                      current.next = ListNode(key, value)
          else:
              self.storage[index] = ListNode(key, value)
  ​
      '''
      Return the value associated with the given key.
      If the key doesn't exist in the hash table, should return -1
      '''
      def get(self, key):
          # Your code here
          # 1. Run our hash function on our key 
          # 2. Check to see if the index is empty or not 
          #   - if it is, return -1 
          #   - otherwise, return the value 
          index = self.hash_fn(key, len(self.storage))
  ​
          if self.storage[index] is None:
              return -1
  ​
          # otherwise, there's a linked list at this index
          # iterate through it to try and find the specified key 
          current = self.storage[index] 
  ​
          while current is not None:
              if current.key == key:
                  return current.value
              
              current = current.next 
  ​
          # we reached the end of the linked list and none of the 
          # keys matched what we were looking for 
          return -1
  ​
      '''
      Removes the key-value pair specified by the key.
      Set the spot where the key-value pair is to None.
      Doesn't return anything.
      '''
      def remove(self, key) -> None:
          # Your code here
          # 1. Run our hash function on our key 
          # 2. Set self.storage[index] = None
          index = self.hash_fn(key, len(self.storage))
  ​
          if self.storage[index] is not None:
              # we need to keep track of both the current node as well 
              # as the previous node 
              # when the current node's key is the one we're looking for 
              # set the previous node's next to refer to current's next 
              # don't forget to check the first node in the linked list 
              if self.storage[index].key == key:
                  # remove the first linked list node 
                  self.storage[index] = self.storage[index].next
                  return 
  ​
              prev = self.storage[index]
              current = prev.next
  ​
              while current is not None:
                  if current.key == key:
                      prev.next = current.next
                      break
  ​
                  prev = current 
                  current = current.next
  ​
  hash_table = MyHashTable(10)
  # ht.put('cat', 'dog')
  # ht.print_storage()
  # ht.put('cat', 'tiger')
  # ht.print_storage()
  ​
  hash_table.put("a", 1)
  hash_table.put("b", 2)
  print(hash_table.get("a"))
  print(hash_table.get("c"))
  hash_table.put("b", 1)         
  print(hash_table.get("b"))
  hash_table.remove("b")         
  print(hash_table.get("b"))
  Collapse


2. *K MOST FREQUENT ELEMENTS FROM A LIST:

  """
  You are given a non-empty list of words.
  ​
  Write a function that returns the *k* most frequent elements.
  ​
  The list that you return should be sorted by frequency from highest to lowest.
  If two words have the same frequency, then the word with the lower alphabetical
  order should come first.
  ​
  Example 1:
  ​
  ```plaintext
  Input:
  words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
  k = 2
  ​
  Output:
  ["lambda", "school"]
      2         2
  Explanation:
  "lambda" and "school" are the two most frequent words.
  ```
  ​
  Example 2:
  ​
  ```plaintext
  Input:
  words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
  k = 4
  ​
  Output:
  ["the", "is", "cloudy", "sky"]
    4     3       2        1
  Explanation:
  "the", "is", "cloudy", and "sky" are the four most frequent words. The words
  are sorted from highest frequency to lowest.
  ```
  ​
  Notes:
  ​
  - `k` is always valid: `1 <= k <= number of unique elements.
  - words in the input list only contain lowercase letters.
  ```
  """
  def top_k_frequent(words, k):
      """
      Input:
      words -> List[str]
      k -> int
  ​
      Output:
      List[str]
      """
      # Your code here
      # we want to figure out the number of occurrences of each word 
      # in the input list 
      word_occurrences = {}    
      # use a hash table to count the occurrence of words in the input list 
      for word in words:
          if word in word_occurrences:
              word_occurrences[word] += 1
          else:
              word_occurrences[word] = 1
  ​
      # we could sort the words by their number of occurrences 
      # in the lambda function, x is the key of the 
      # we can have our lambda function return a tuple to represent 
      # the priority for how we want to sort 
      sorted_words = sorted(word_occurrences, key=lambda k: (-word_occurrences[k], k))
  ​
      # grab the top k words 
      return sorted_words[:k]
  ​
  words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
  print(top_k_frequent(words, 4))
  ​
  words = ["lambda", "achool", "rules", "lambda", "achool", "rocks"]
  print(top_k_frequent(words, 2))



3. SORT STR OF CHARS BASED ON FREQ:

  """
  Given a string, sort it in decreasing order based on the frequency of characters.
  ​
  Example 1:
  ​
  ```plaintext
  Input:
  "free"
  ​
  {
      'f': 1,
      'r': 1,
      'e': 2,
  }
  ​
  Output:
  "eefr"
  ​
  Explanation:
  'e' appears twice while 'f' and 'r' appear once.
  So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
  ```
  ​
  Example 2:
  ​
  ```plaintext
  Input:
  "dddbbb"
  ​
  Output:
  "dddbbb"
  ​
  Explanation:
  Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
  Note that "dbdbdb" is incorrect, as the same characters must be together.
  ```
  ​
  Example 3:
  ​
  ```plaintext
  Input:
  "Bbcc"
  ​
  Output:
  "ccBb"
  ​
  Explanation:
  "ccbB" is also a valid answer, but "Bbcc" is incorrect.
  Note that 'B' and 'b' are treated as two different characters.
  ```
  """
  ​
  from collections import Counter
  ​
  # def frequency_sort(s: str) -> str:
  #     counts = Counter(s)
  ​
  #     letter_frequencies = counts.most_common()
  ​
  #     return ''.join(letter * freq for letter, freq in letter_frequencies) 
  ​
  def frequency_sort(s: str) -> str:
      """
      Inputs:
      s -> str
  ​
      Output:
      str
      """
      # Your code here
      # we want to count the number of occurrences of individual letters 
      # in the input word 
      letter_occurrences = {}
  ​
      for letter in s:
          if letter in letter_occurrences:
              letter_occurrences[letter] += 1
          else:
              letter_occurrences[letter] = 1
  ​
      letter_occurrences = letter_occurrences.items()
  ​
      # we want to reconstruct the input word with letters that show up more 
      # frequently ordered first 
      sorted_letters = sorted(letter_occurrences, key=lambda t: -t[1])
      # [('e', 2), ('f', 1), ('r', 1)]
  ​
      # we want to take the letters in `sorted_letters` and construct a string out
      # of them 
      # construct the final string 
      # using a comprehension
      # return ''.join(letter * freq for letter, freq in sorted_letters)
  ​
      final_string = ''
  ​
      for letter, freq in sorted_letters:
          final_string += (letter * freq)
  ​
      return final_string
  ​
  word = "free"
  print(frequency_sort(word))
  ​
  word = "Bbcc"
  print(frequency_sort(word))