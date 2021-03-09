1. HASH TABLES INTRO:

  TC: (BEST CASE/WORST CASE) = O(1) / O(n)
  SC: O(n)

  Strengths: 
    O(1) average lookup etc. 
    Can use any hashable object as key

  Weakness:
    mapping goes one way so unless you know the key its going to be innefficient to find the value


2. DESCRIBE AND IMPLEMENT A HASH FUNCTION:

  def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size


3. IMPLEMENT A HASH TABLE CLASS:

  class HashTable:
      """
      A hash table with `capacity` buckets
      that accepts string keys
      """

      def __init__(self, capacity):
          self.capacity = capacity  # Number of buckets in the hash table
          self.storage = [None] * capacity
          self.item_count = 0

      def djb2(self, key):
          """
          DJB2 hash, 32-bit
          """
          # Cast the key to a string and get bytes
          str_key = str(key).encode()

          # Start from an arbitrary large prime
          hash_value = 5381

          # Bit-shift and sum value for each character
          for b in str_key:
              hash_value = ((hash_value << 5) + hash_value) + b
              hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

          return hash_value

      def hash_index(self, key):
          """
          Take an arbitrary key and return a valid integer index
          between within the storage capacity of the hash table.
          """
          return self.djb2(key) % self.capacity

      def put(self, key, value):
          """
          Store the value with the given key.
          """
          index = self.hash_index(key)
          self.storage[index] = value
          return

      def delete(self, key):
          """
          Remove the value stored with the given key.
          """
          index = self.hash_index(key)
          self.storage[index] = None

      def get(self, key):
      """
          Retrieve the value stored with the given key.
          Returns None if the key is not found.
          """
          index = self.hash_index(key)
          return self.storage[index]

