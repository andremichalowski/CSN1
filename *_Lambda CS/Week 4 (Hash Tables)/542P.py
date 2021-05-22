1. HOW TO COMPUTE LOAD FACTOR:

    >>>> The number of items stored in a hash table divided by the total number of slots.

2. IMPORTANCE OF LOAD FACTOR OF HASH TABLE:

    >>>> As the load factor of your hash table increases, so does the likelihood of a collision,
    which reduces your hash table's performance. It is important to monitor the load
    factor and resize your hash table when the load factor gets too large. 

3. ISOMETRIC STRINGS:

  Given two strings a and b, determine if they are isomorphic.

  Two strings are isomorphic if the characters in a can be replaced to get b.

  All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.


  def csIsomorphicStrings(a, b):
      return [a.find(i) for i in a] == [b.find(j) for j in b]

4. WORD PATTERN:

  Given a pattern and a string a, find if a follows the same pattern.

  Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in s.

  def csWordPattern(pattern, a):
      s = pattern
      t = a.split()
      return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

  
5. GROUP ANAGRAMS:

Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different wo

  def csGroupAnagrams(strs):
      anas = {}
      for string in strs:
          s = ''.join(sorted(string))
          if s in anas:
              anas[s].append(string)
          else:
              anas[s] = [string]
      return [ anas[x] for x in anas ]