1. REVERSE STRING IN PLACE:

  for i in range(len(s)//2):
    s[i], s[-i-1] = s[-i-1], s[i]


2. REVERSE INT W/SIGNS:
  class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        symbol = 1
        
        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x //= 10
            
        return 0 if result > pow(2,31) else result * symbol


3. FIRST UNIQUE CHARACTER: (HASH MAP)

  count = collections.Counter(s)
 
  for idx, ch in enumerate(s):
      if count[ch] == 1:
          return idx     
  return -1


4. ANAGRAM:

  if len(s) != len(t):
    return False
  return sorted(s) == sorted(t)


5. 