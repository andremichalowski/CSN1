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

2. 