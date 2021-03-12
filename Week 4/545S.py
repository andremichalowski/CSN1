1. CONDENSED LL:

Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    current = node
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return node
    
    # current = node
    # while current:
    #     while current.next and current.next.value == current.value:
    #         current.next = current.next.next    
    #     current = current.next     
    # return node

     # first, second = node, node.next if node else None
    # while second:
    #     if first.value == second.value:
    #         second = second.next
    #         first.next = second
    #     else:
    #         first = second
    #         second = second.next
            
    # return node
    
    
    # current=node
    # while node:
    #     while node.next and node.next.value==node.value:
    #         node.next=node.next.next
    #     node=node.next
    # return node

       
    # current = node
    # singles = {}
    
    # if current:
    #     singles[current.value] = 1
    #     print(singles, 'start')
    # while current and current.next:
    #     if current.next.value not in singles:
    #         print('new next value---')
    #         print(current.value, 'current')
    #         print(current.next.value, 'next')
    #         singles[current.next.value] = 1
    #     else:
    #         print('cutting', current.next.value)
    #         current.next = current.next.next
    #     print(singles, 'moving')
    #     current = current.next
    
    # return node

2. FIRST NON REPEATING CHARACTER:

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# from collections import Counter, collections


def first_not_repeating_character(s):
    
    dic = {}
    for char in s:
        dic[char] = dic.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if dic[char] and dic[char] == 1:
            return char
    return "_"
    
    # if not s: return "_"
    # d = collections.defaultdict(int)
            
    # for char in s:
    #     d[char] += 1
                
    # for i, c in enumerate(s):
    #     if d[c] < 2:
    #             return i
    # return "_"

   
    # d = {}
    # seen = set()
    # for idx, c in enumerate(s):
    #     if c not in seen:
    #         d[c] = idx
    #         seen.add(c)
    #     elif c in d:
    #         del d[c]
    # return min(d.values()) if d else "_"
        
        
    # counter = Counter(s)
    # for i, char in enumerate(s):
    #     if counter[char] == 1:
    #         return i
    # return '_'   
    
    
    # d = {}
    # for l in s:
    #     if l not in d: d[l] = 1
    #     else: d[l] += 1
    
    # index = -1
    # for i in range(len(s)):
    #     if d[s[i]] == 1:
    #         index = i
    #         break
    
    # return index


3. UNDERCOVER SPY:

In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.


def uncover_spy(n, trust):
    trusted = [0] * (n+1)
    for a, b in trust:
        trusted[a] -= 1
        trusted[b] += 1

    for i in range(1, n+1):
        if trusted[i] == n-1:
            return i
    return -1