1. REVERSE STRING:

Given a string (the input will be in the form of an array of characters), writ

def csReverseString(chars):
    return chars[::-1]

My approach involved using the step portion of split functionality to reverse the order of the string. There were no obstacles or difficulties, this is something that I used frequently and often.

My approach has O(n) complexity because the size and time of the result has a direct relationship to the input. The size of the string or list that is input will have a proportional effect as it increases or changes. This can not be improved because it is using the minimum methods and minimum lines of logic possible to make this change.

2. PALINDROME:

Codewriting

A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

def csCheckPalindrome(input_str):
    #INPUT: input_str
    #OUTPUT: boolean for palindrome result
    
    #conditional checking if forwards is the same backwards
        #return true if so
        
    if input_str == input_str[::-1]:
        return True
    else:
        return False

My process involved using the U.P.E.R. approach to problem solving. 
1. Understand: Understand what the question is asking. - For this step I reviewed the question carefully asking questions about what to expect, questions about input and output, how complex it might be, and what the size of the problem might be. This step usually involves me writing out the input and output as well. 
2. Plan: What steps are involved to solve the problem. - For this step I try my best to think of how to solve the problem in a broad conceptual way and then refine my approach to add specific methods that I know of or atleast brainstorm how they might be used to solve it. This step usually involves writing psuedo-code to reflect these plans or ideas.
3. Execute: Convert plan to actual code. - In this step I carry out the plan that I committed to from the planning stage. 
4. Reflect: Asking is the solution optimal. - For this step I try to review if the solution is solved in the most efficient and readable way possible. If it isn't I try my best to change it. 

My plan and execution involved simply understanding that a palindrome is the same word if it is reversed. Using similar logic as the first prompt plus an additional conditional I was able to check if the presentation of the string is the same in reverse as it is in it's original form.

The time and space complexity for this solution is O(1) because there is a constant relationship between the input and the output result. No matter how many characters are involved or the size of the string involved for the input of the function the output will always be a single boolean result. 

3. DUPLICATES IN A STRING:

Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

def csRemoveDuplicateWords(input_str):
    #INPUT: String of words
    #OUTPUT: String with no duplicate words
    
    #Init result list
    #make individual words items in array w/split
    #iterate through array 
        #conditional comparing previous entry from init result list with current string index
        #append if passes skip if not
        
    result = []
    words = input_str.split()    
    for i in words:
        if i in result:
            continue
        elif i not in result:
            result.append(i) 
    return " ".join(result)

    
        # if i == result[len(result)-1]:
        #     continue
    #     elif i != result[len(result)-1]:
    #         result.append(i)
    
    # return "".join(result)
    
My process involved using the U.P.E.R. approach to problem solving. 
1. Understand: Understand what the question is asking. - For this step I reviewed the question carefully asking questions about what to expect, questions about input and output, how complex it might be, and what the size of the problem might be. This step usually involves me writing out the input and output as well. 
2. Plan: What steps are involved to solve the problem. - For this step I try my best to think of how to solve the problem in a broad conceptual way and then refine my approach to add specific methods that I know of or atleast brainstorm how they might be used to solve it. This step usually involves writing psuedo-code to reflect these plans or ideas.
3. Execute: Convert plan to actual code. - In this step I carry out the plan that I committed to from the planning stage. 
4. Reflect: Asking is the solution optimal. - For this step I try to review if the solution is solved in the most efficient and readable way possible. If it isn't I try my best to change it. 

More specifically my approach involved the UPER approach to analyze, understand input and outputs, and write psuedo-code. The psuedo code I wrote reflected some concept of an array being needed as a result for the final computation, the conditional logic that reviews if the array contains the string that is being iterated from the split input and the resulting logic that appends the strings that do not exist, and the final return statement that joins the strings in the array back together.  

The time and space complexity of this solution is O(n) because the relationship that exists between the input and output in most scenarios involving this formula is going to be direct and linear. In some cases there will be more or less duplicates which would mean the relationship is not consistently direct but it is closer to this relationship than a constant relationship or a logarithmic relationship. As the input increases the output size will typically gradually increase. 