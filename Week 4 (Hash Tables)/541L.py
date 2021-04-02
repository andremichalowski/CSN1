1. CREATE YOUR OWN HASHTABLE WITHOUT LIBRARY:

def hash_fn(key, length):
    return id(key) % length
class MyHashTable:
    def __init__(self, capacity, hash_fn=hash_fn):
        self.storage = [None] * capacity
        self.hash_fn = hash_fn
​
    def print_storage(self):
        print(self.storage)
​
    '''
    Add the key and value as a pair in the hash table. 
    If the value already exists in the HashTable, update the value.
    '''
    def put(self, key, value):
        index = self.hash_fn(key, len(self.storage))

        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] = (key, value) # O(1)
            else:
                old_key, old_val = self.storage[index]
                print(f"Collision! Overwriting {old_key}: {old_val}")
                self.storage[index] = (key, value)
​
        self.storage[index] = (key, value)
​
    def get(self, key):
        index = self.hash_fn(key, len(self.storage))

        if self.storage[index] is None:
            return -1
        return self.storage[index][1]
​
    def remove(self, key) -> None:
     
        index = self.hash_fn(key, len(self.storage))
​
        self.storage[index] = None # O(1)
​
​
hash_table = MyHashTable(10)

hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a"))
print(hash_table.get("c"))
hash_table.put("b", 1)         
print(hash_table.get("b"))
hash_table.remove("b")         
print(hash_table.get("b"))
Collapse

2. ARE WORDS SORTED:

def are_words_sorted(words, alpha_order):
    lookup_table = {} # doing the same thing (creating a lookup table) using a comprehension # lookup_table = {letter: index for index, letter in enumerate(alpha_order)}
    for index, letter in enumerate(alpha_order):
        lookup_table[letter] = index
    # do an is_sorted check but refer to the alternate ordering instead 
    return is_sorted(words, lookup_table)
​
def is_sorted(words, lookup_table):
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
​
        length_of_shorter_word = min(len(word1), len(word2))
​
        for k in range(length_of_shorter_word):
            letter1 = word1[k]
            letter2 = word2[k]
​
            if lookup_table[letter1] > lookup_table[letter2]:
                return False 
                
        if len(word1) > len(word2):
            return False 
​
    return True