1. LINKED LIST:

https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm

https://www.tutorialspoint.com/data_structures_algorithms/doubly_linked_list_algorithm.htm

https://www.tutorialspoint.com/data_structures_algorithms/circular_linked_list_algorithm.htm

Head, Tail, Link

Single, Double, Circular 


  1. COMPLEXITY:
    TIME:
      Lookup: O(n)
      Append: O(1)
      Insert: O(n)
      Delete: O(n)
    SPACE:
      ...: O(n)

  2. STRENGTHS + WEAKNESSES:
    S: Appending heads or tails...general
    W: Accessing at middle

  3. DIFFERENCES BETWEEN ARRAYS AND LINKEDLISTS:
    - Arrays: use contiguous(side by side) memory
    - LinkedLists: Stores data + pointer to next data

  4. MAKING LINKED LISTS:

    A1. Linked List Node Class

      class LinkedListNode:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    A2. Linked List Class

      class LinkedList:
        def __init__(self, head=None):  
            self.head = head

        def append(self, data):
            new_node = LinkedListNode(data)

            if self.head:
                current = self.head

                while current.next:
                    current = current.next

                current.next = new_node
            else:
                self.head = new_node

    B. Create a List:
      >>> a = LinkedListNode(1)
      >>> my_ll = LinkedList(a)
      >>> my_ll.append(2)
      >>> my_ll.append(3)
      >>> my_ll.head.data
      1
      >>> my_ll.head.next.data
      2
      >>> my_ll.head.next.next.data
      3
      >>>

    