1. IF A QUEUE ONLY ALLOWS OPERATIONS AT THE ENDS (FRONT AND BACK), WHAT OTHER DATA STRUCTURE WOULD WORK PERFECTLY TO USE TO BUILD THE QUEUE?
  1. Linked List1


2. STRENGTH OF A STACK DATA STRUCTURE:
  1. The strength of a stack data structure is that all operations are fast take O(1) amount of time.


3. QUEUE ON STACKS:

# Implement a queue using two stacks.

# You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" operation that is performed.

# Example

# For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
# queueOnStacks(requests) = [1, 2].

# After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        right.push(x)

    def remove():
        left.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


4. VALID BRACKET SEQUENCE:

# Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

# The Valid bracket sequence is defined in the following way:

# An empty bracket sequence is a valid bracket sequence.
# If S is a valid bracket sequence then (S), [S] and {S} are also valid.
# If A and B are valid bracket sequences then AB is also valid.

def validBracketSequence(sequence):

    stack = [] 
  
    for char in sequence: 
        if char in ["(", "{", "["]: 
            stack.append(char) 
        else: 
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
  
        if stack: 
            return False
        return True
