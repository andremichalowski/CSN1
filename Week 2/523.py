1. "QUEUE"

  1. FIFO

  2. Space + Time Complexity:
    - Space = O(n)
    - Time = O(1)

    Enqueue - add item to back 
    Dequeue - remove item from front
    Peek - inspect item from front of queue

  3. Strengths + Weaknesses:
    - S: O(1)
    - W: None
    

2. "STACK"

  1. LIFO

  2. Space + Time Complexity:
    - Space = 0(n)
    - Time = O(1)

    Push - add to top
    Pop - remove from top
    Peek - inspect top

  3. Strengths + Weaknesses:
    - S: O(1)
    - W: None (not very versatile though...?)


3. IMPLEMENT A QUE USING A LL:

   1. Create LLN:
      class LinkedListNode:
        def __init__(self, data):
          self.data = data
          self.next = None


    2. Create QUE:

      class Queue:
        def __init__(self):
          self.front = None
          self.rear = None


    3. Define enqueue method:

        def enqueue(self, item):
          new_node = LinkedListNode(item)
          # check if que is empty
          if self.rear is None:
            self.front = new_node
            self.rear = new_node
          else: 
            # add new node to rear
            self.rear.next = new_node
            # reassign rear to new node
            self.rear = new_node

    4. Define dequeue method:


        def dequeue(self):
          # check if queue is empty
          if self.front is not None:
            # keep copy of old front
            old_front = self.front 
            self.front = old_front.next

          # check if que now epty
          if self.front is None:
            self.rear = None

          return old_front


4. IMPLEMENT A STACK USING A DYNAMIC ARRAY:

  1. Define stack class and __init__ method:

    class Stack:
      def __init__(self):
        self.data = []

  2. Define a push method to add an item to the top of stack:

      def push(self, item):
          self.data.append(item)

  3. Define a pop method to remove an item from the top of stack:

      def pop(self, item):
          if len(self.data) > 0:
            return self.data.pop()
          return "The stack is empty"


5. IMPLEMENT A STACK USING A LINKED LIST:

  1. Define stack and __init__ method:

    class LinkedListNode:
      def __init__(self, data):
        self.data = data
        self.next = None

    class Stack:
      def __init__(self):
        self.top = None

  2. Define push method to add to top of stack:

      def push(self, data):
        # create new node with data
        new_node = LinkedListNode(data)
        # set current top to new node's next
        new_node.next = self.top
        # reset the top pointer to the new node
        self.top = new_node

  3. Define a pop method to add to bottom

      def pop(self):
        # make sure stack is not empty
        if self.top is not None:
          # store popped node
          popped_node = self.top
          # reset top pointer to next node
          self.top = popped_node.next
          # return the value from the popped node
          return popped_node.data


    

