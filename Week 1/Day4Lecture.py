Sean Chen: https://www.youtube.com/watch?v=X1jTAe1tgWA

1. RETURN STRING TO LOWERCASE

def to_lower_case(string):
    ascii_values = [ord(l) for l in string] # O(n) time, O(n) space 
    for i, v in enumerate(ascii_values): # O(n) time 
        if 65 >= v and v <= 90: 
            ascii_values[i] += 32 
    return ''.join(chr(v) for v in ascii_values)
print(to_lower_case("LambdaSchool"))


".lower()" method: https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python



2. RETURN THE NUMBER OF 1'S IN AN INT 
​
def hamming_weight(n):
   (n).count('1')
​
    bin_rep = bin(n)
    counter = 0
​
    for digit in bin_rep:
        if digit == '1':
            counter += 1
​
    return counter 
​
print(hamming_weight(201))
print(hamming_weight(4294967291))
​