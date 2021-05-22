1. RETRIEVES LAST N ELEMENTS FROM A LIST:
def last(a, n):
    return a[-n:]


2. INDEX ADDED TO ITSELF:
def add_indexes(numbers):
    return [numbers.index(number) + number for number in numbers]


3. RETURN PROD OF NUMBERS IN A LIST:
def multiply_nums(nums):
    split = nums.split(', ')
    ints = [] 
    for digit in split:
        ints.append(int(digit))
    return math.prod(ints)


4. CHANGE TEXT TO EMOJIS:
def emotify(txt):
    words = txt.split(' ')
    last_word = words[-1]

    associations = {
        "smile": ":D",
        "mad": ">:(",
        "grin": ":)",
        "sad": ":("
    } 

    words[-1] = associations[last_word]
​
    return ' '.join(words)


5. RETURN DATA TYPE OF A GIVEN ARGUEMENT:
def data_type(value):
    types = {
        "list" : "list", #ETC
    }
    data_type = str(type(value).__name__)#get type (type form)
    return types[data_type_st]


6. RETURN NUMBER COUNT OF VOWELS IN STRING:

def get_count(input_str):
    vowels = "aeiou"
    counter = 0 
    for letter in input_str.lower():
        if letter in vowels:
            counter += 1
    return counter 


7. STRING CHAR EXPONENTIAL GROWTH:
def repeat_it(input_str):
    result = ""
    for i in range(len(input_str)):
        curr_char  = input_str[i] #destructured
        result += curr_char.upper()
        result += curr_char.lower() * i
        result += "-" #conditional for last statement only (instead of slice)
    return result[:-1]


8. EVEN / ODD EVALUATOR:
def parity(input_int):
    if input_int % 2 == 0:
        return "Even"
    else: 
        return "Odd"


9. RETURN MIDDLE CHAR/S OF WORD:
def get_middle(input_str):
    midpoint = (len(input_str) - 1) // 2
    if len(input_str) % 2 == 0:
        return input_str[midpoint : midpoint + 2]
    return input_str[midpoint]
