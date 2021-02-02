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


5. VALID PALINDROME:

  def isPalindrome(self, s: str) -> bool:
    # nS = s.replace("\W+", "")
    # return nS[0:(len(s)//2)] == nS[(len(s)//2):(len(s))]
    
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s==s[::-1]


6. STRING TO INTEGER: (ATOI):

7. IMPLEMENT strStr():

8. SEE AND SAY: (How many repeats of each num):

  def countAndSay(self, n):
      # The first char of our result is 1 so initilize the result
      s = '1'
      
      # As we have taken care of case 1 with n == 1 we start from 2
      while n > 1:
          
          i = 0
          # create new string every iteration and assign it to our res
          ns = ''
          while i < len(s):
              # As we already included the first character so count = 1
              count = 1
              # Check if the prev char is same as next and keep count
              while i+1 < len(s) and s[i] == s[i+1]:
                  i += 1
                  count += 1
              # Finally make the new string
              ns += str(count) + s[i]
              i += 1
          # Assign the newly made string for next iteration to s
          s = ns
          n -= 1
      return s


return countAndSay(34556)


9. STRING TO INTEGER: (Atoli Way):

def myAtoi(self, str: str) -> int:
    intval=0
    try:
        intval=int(str)
    except:
        str=str.strip()
        nums=0
        coms=0
        for index, ele in enumerate(str):
            if (ele=='-' or ele=='+') and coms==0: nums+=1
            elif ele not in ('0','1','2','3','4','5','6','7','8','9') or nums>1:
                try:
                    intval = int(str[:index])
                    break
                except:
                    intval = 0
                    break
            else:
                coms+=1
    if intval<=-2**31: return -2**31
    elif intval>=2**31-1: return 2**31-1
    else: return intval


10. NEEDLE IN A HAYSTACK: IMPLEMENT strStr(): 

def strStr(self, haystack: str, needle: str) -> int:
    # return haystack.find(needle)
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

    http://tpcg.io/viJ4qzqG
