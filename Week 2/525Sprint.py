1. REVERSE LINKED LIST:

Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    new_l = None
    while l:
        l.next, l, new_l = new_l, l.next, l
    return new_l



2. CHECK BLANAGRAMS:

Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.


# def checkBlanagrams(word1, word2):
import re

def checkBlanagrams(str1, str2):
    if len(str1) != len(str2): 
        return False
    miss_count = 0
    char_dict = {}
    for character in str1:
        char_dict[character] = 0
    for character in str2: 
        if character not in char_dict: 
            miss_count += 1
        else: 
            char_dict[character] += 1
    for value in char_dict.values(): 
        if value == 0:
            miss_count += 1
    return (miss_count == 1 or miss_count == 2)



3. FIND VALUE SORTED SHIFTED ARRAY:
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1



def findValueSortedShiftedArray(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return nums.index(nums[mid])
        
        if nums[mid] >= nums[left]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
