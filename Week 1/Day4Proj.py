1. CPU COMMUNICATES WITH RAM VIA THE WHAT?

  Memory Bus


2. PROCESSOR GETS SPEED BOOST WHEN PROCESSOR ACCESSES NEARBY SEQUENTIAL MEMORY ADDRESSES:

  Because of the cache.


3. GIVEN NUMBER 96, CONVERT INTO BINARY, THEN ADD RESULTING DIGITS IN DECIMAL. WHAT IS THE RESULT:

  2


4. *TIME* COMPLEXITY OF PERFORMING MATHEMATICAL OPERATIONS ON FIXED-WIDTH INTEGERS?
   *SPACE* COMPLEXITY OF FIXED-WIDTH INTEGERS?

  0(1)


5. IN EACH SLOT MEMORY HOLDS 8 BITS AND WE WANT TO STORE AN ARRAY OF 64-bit INTEGERS, 
   HOW MANY MEM ADDRESSES WILL BE REQUIRED TO STORE AN ARRAY OF 5 INTEGERS?

  40


6. IN ORDER TO STORE STRINGS IN MEMORY, EACH CHARACTER IN THE STRING MUST BE ENCODED SO THAT IT CAN BE STORED AS BINARY. ASCII IS ONE EXAMPLE OF A CHARACTERS. SET. EACH CHARACTER IN ASCII CAN BE REPRESENTED BY 7 BITS (ALTHOUGH THEY ARE COMMONLY STORED AS 8 BITS). GIVEN THAT, WHAT IS THE MASXIMUM NUMBER OF CHARACTERS THAT COULD BE IN THE ASCII SET?

  128

7. INT, REVERSE, RETURN INT
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

  def csReverseIntegerBits(n):
    binary = bin(n)[2:] #0b110100001 #([2:] 110100001)
    reverse = binary[::-1] #100001011b0
    integer = int(reverse, 2)
    return(integer)


8. CS BINARY TO ASCII:
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

def csBinaryToASCII(binary):
    if binary == "":
        return ""
    str_bin = str(binary)
    split_binary = [str_bin[i:i+8] for i in range(0, len(str_bin), 8)]
    decoded_str = ""
    for bin_letter in split_binary:
        letter = chr(int(bin_letter, 2))
        decoded_str += letter
    return decoded_str


9. RETURNS CERTAIN STRINGS BASED ON IF IT HAS A FACTOR OF A NUMBER:
Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

  def csRaindrops(number):
    #INPUT: Number
    #OUTPUT: strings based on if it is a factor or not
    
    #Create result array
    #Test if factor of 3
        # push string if factor of 3
    #Test if factor of 5
        # push string if factor of 5
    #Test if factor of 7
        # push string if factor of 7
    #If none 
        #return digits of number as string
        
    #join rain sounds
    #return array at 0
    
    raindrop_sounds = []
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        if number % 3 == 0:
            raindrop_sounds.append("Pling")
        if number % 5 == 0:
            raindrop_sounds.append("Plang")
        if number % 7 == 0:
            raindrop_sounds.append("Plong")
        joined = "".join(raindrop_sounds)
        return joined
    else:
        return str(number)
        

print(csRaindrops(105))





