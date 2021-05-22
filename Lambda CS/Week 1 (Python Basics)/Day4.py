1. RAM:

Random access memory

Processor, memory controller, RAM

2. DECIMAL TO BINARY:

Each successive digit in the base 10 number system is a power of ten. The ones place is 10^0 = 1. The tens place is 10^1 = 10. The hundreds place is 10^2 = 100. This pattern continues on and on.

Decimal	Binary
0	0000
1	0001
2	0010
3	0011
4	0100
5	0101
6	0110
7	0111
8	1000

3. FIXED WIDTH INTEGERS STORED IN MEMORY:

We now know that things are stored in RAM using binary, and each "box" in RAM holds 1 byte (8 bits). What does that mean for what we can store in RAM? Let's say we have 1 byte of RAM to use. How many different numbers can we represent using only this 1 byte?

Remember that each digit in a binary number is a successive power of 2. If we have 8 bits to use, we can store 2^8 = 256 different numbers in 1 byte.

Let's see if we can find a pattern:

With one bit, we can express two numbers (0 and 1)
With two bits, for each of the first numbers (0 or 1), we can put a 0 or a 1 after it, so we can express four numbers
With three bits, we can express eight numbers.
Every time we add a new bit, we double the number of possible numbers we can express in binary. This pattern can be generalized as 2^n and 2^8 = 256.

Often, computers use 4 bytes (32 bits) to represent our variables, meaning that we can express as many as 4 billion (2^32) possible values. Similarly, computers may use 8 bytes (64 bits) to represent our variables and can express over 10 billion (2^64).

The 2^X in the binary number system is called the bitsize. Eight bytes of memory are called "8-bit", and 16 bytes are called "16-bit," etc.

In theory, you could use less space to represent smaller integers. For instance, in binary, the number one is represented by 1. So, technically, to store one in binary, you only need one bit. But computers don't usually do this. Many integers take a fixed amount of space, no matter what number they might have in them. So, even though you only need one bit to represent the number one, the computer would still use 32 or 64 bits to do so.

So, if a variable represents a fixed-width integer, it doesn't matter if it has the value 0 or 123,456; the amount of space it takes up in RAM is the same.

The computer can store numbers like 3, 60000000, or -14 in 32 bits, one of the "fixed-width integers" we discussed earlier. All of these fixed-width integers take up constant space (O(1)).

Storing numbers as fixed-width integers introduces a trade-off. We have constant space complexity, and because each integer has a constant and expected number of bits, simple mathematical operations only take constant time. The cost of having an integer as fixed-width is that there is a limit to the number of integers you can represent.


4. GENERAL TERMS HOW ARRAYS ARE STORED IN MEMORY AND TIME COMPLEXITY OF LOOKUPS:

Looking up an index is like going to a house address.


5. CHARACTER ENCODING AND HOW STRINGS ARE STORED IN MEMORY:

o use our 8-bit slots in memory, we need a way to encode each character in a string in 8-bits. One common character encoding to do this is called "ASCII". Here's how the alphabet is encoded in ASCII:

Letter	Encoding
A	01000001
B	01000010
C	01000011
D	01000100
E	01000101
F	01000110
G	01000111
H	01001000
I	01001001
J	01001010
K	01001011
L	01001100
M	01001101
N	01001110
O	01001111
P	01010000
Q	01010001
R	01010010
S	01010011
T	01010100
U	01010101
V	01010110
W	01010111
X	01011000
Y	01011001
Z	01011010