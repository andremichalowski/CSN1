1. VALID PHONE NUMBERS:
  # Description - https://leetcode.com/problems/valid-phone-numbers/
  # Discussion - https://leetcode.com/problems/valid-phone-numbers/discuss/?currentPage=1&orderBy=most_votes&query=
  # Bash Script Overview - https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php
  # RegEx Reference - https://regexr.com/


  # Short Version:
    egrep "^(\([0-9]{3}\) |[0-9]{3}\-)[0-9]{3}\-[0-9]{4}$" file.txt


2. REVERSE INTEGER:
  # Description: https://leetcode.com/problems/reverse-integer/
  # Discussion: https://leetcode.com/problems/reverse-integer/discuss/?currentPage=1&orderBy=most_votes&query=

  # Solution: 
  def reverse(self, x):
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

3. BUDDY STRINGS:
