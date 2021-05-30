1. "DOES MY NUMBER LOOK BIG IN THIS" (DETECT IF NUMBER IS NARCISSISTIC (SUM OF OWN DIGITS EACH RAISED TO POWER OF NUMBER OF DIGITS IN BASE)):
  # PROBLEM: https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
  
  # SUDO:
    # SET VARIABLE = VALUE
    # SPLIT VARIABLE INTO INDIVIDUAL INTS...ARRAY?
    # ITERATE THROUGH ARRAY * NUMBER OF DIGITS IN OG VALUE
    # CONDITIONAL TRUE IF EACH INT ^ #DIGITS = VALUE


  # 1. I make an array with the value. But I need to transform it to string first to make it happen. I build an array so I can iterate over each element.
  # 2. I create a variable `_result` who is a data store of the value.
  # 3. Loop over each value and need to transform back the value to a number so I can make some Math with it.
  # 4. I use Math.pow you give me the power of a number. The second arguments I use is the length of the value. So if the number is `123` the pow become `1^3 2^3 3^3`
  # 5. I make sure to add the value to the _result data store.
  # 6. We need to return only a boolean about if this is match or not.

  ### Solution
  ```js
    function narcissistic(value) {
      const _value = String(value).split('');

      let _result = 0;

      for (ch of _value) {
        const num = parseInt(ch, 0)

        _result += Math.pow(num, _value.length);
      }

      return _result === value;
    }
  ```

  # PSUEDO Repetition:
    # 1. make an array with individual string values by converting to string and spliting
    # 2. set result for recursive additions later
    # 3. loop over characters
      # 4. set variable to integer versions of character using 'parseInt'
      # 5. recurssive additions to result with 'Math.pow() using "num" and "value.length" '
    # 6. return true or false check for result === value?

  