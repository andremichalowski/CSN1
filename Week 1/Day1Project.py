csWhereIsBob

Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
Notes:

Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").

def csWhereIsBob(names):

#INPUT: List of names
#OUTPUT: Location of "Bob" in list

#If "Bob" exists in list return index
#elif "Bob" does not exist return -1

    if "Bob" in names:
        return names.index("Bob")
    elif "Bob" not in names:
        return -1

-------------------------------------------

CsAlphanumericRestriction

Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True

def csAlphanumericRestriction(input_str):
#INPUT: String
#OUTPUT: True if only numbers or only characters >>> False if numbers and letters

#use isalpha() method to determine if all alpha then true 

    if input_str.isalpha() or input_str.isnumeric():
        return True
    else:
        return False

---------------------------------------------

csOppositeReverse

Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"

def csOppositeReverse(txt):
#INPUT: txt (a string)
#OUTPUT: txt reverse txt camel
    return txt[::-1].swapcase()


---------------------------------------------

csSquareAllDigits

Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9

def csSquareAllDigits(n):

#split integer
#loop split integer
#square each value

    # int_to_string = str(n) #123 >> "123"

    # split_strings = int_to_string.split() # ["1", "2", "3"]
    
    # strings_to_ints_squared = [int(string)**2 for string in split_strings] [1, 4, 9]
    
    # ints_back_to_strings = [str(int) for int in strings_to_ints_squared] # CONVERTED TO STRINGS AND THEN CONCATeNATED

    # ints_joined_stringed = "".join(ints_back_to_strings)
    
    # stringed_back2intsagain = int(ints_joined_stringed)
    
    # return stringed_back2intsagain
    
    return int(''.join([str(int(i)**2) for i in str(n)]))
    
    

---------------------------------------------

csSchoolYearsAndGroups

Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
Notes:

1 <= years <= 10
1 <= groups <=26

def csSchoolYearsAndGroups(years, groups):
    # scl_grps = []
    
    # for year in years:
    #     for group in groups:
    #         scl_grps.append(str(year) + (str(chr(65+group))))
            
    # return scl_grps
    
    
    # results= ""
    
    # for year in range(1, years + 1):
    #     for group in [chr(i) for i in range(ord('a'), ord(chr(97 + groups)))]:
    #         results += (str(year) + group + ", ")
    
    # return results
    
    
            
    results= ""
    
    for year in range(1, years + 1):
        for group in [chr(i) for i in range(ord('a'), ord(chr(97 + groups)))]:
            results += (str(year) + group + ", ")
    
    return results[:-2]
    
    


---------------------------------------------

csMakeItJazzy

Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []

def csMakeItJazzy(chords):
    result = []
    
    for chord in chords:
        
        if chord.endswith("7"):
                result += [chord]
                
        else:
            result.append(chord + "7")
    
    return result


---------------------------------------------



