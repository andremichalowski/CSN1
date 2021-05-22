1. PUT METHOD FOR COLLISIONS:

  def put(self, key, value):
      """
      Store the value with the given key.
      Hash collisions should be handled with Linked List Chaining.
      Implement this.
      """
      index = self.hash_index(key)

      current_entry = self.storage[index]

      while current_entry is not None and current_entry.key != key:
          current_entry = current_entry.next

      if current_entry is not None:
          current_entry.value = value
      else:
          new_entry = HashTableEntry(key, value)
          new_entry.next = self.storage[index]
          self.storage[index] = new_entry

2. LOAD FACTOR AND RESIZING BASED ON LOAD FACTOR SIZE:

  def put(self, key, value):
      """
      Store the value with the given key.
      Hash collisions should be handled with Linked List Chaining.
      Implement this.
      """
      index = self.hash_index(key)

      current_entry = self.storage[index]

      while current_entry is not None and current_entry.key != key:
          current_entry = current_entry.next

      if current_entry is not None:
          current_entry.value = value
      else:
          new_entry = HashTableEntry(key, value)
          new_entry.next = self.storage[index]
          self.storage[index] = new_entry

          self.item_count += 1

          if self.get_load_factor() > 0.7:
              self.resize(self.capacity * 2)