SEAN CHEN DECEMBER 9TH QUEST AND STACKS: https://youtu.be/rwJFhD1XBFU

1. QUEUE USING LL:
  class Node:
      def __init__(self, val):
          self.val = val
          self.next = None
  ​
  class Queue:
      def __init__(self):
          # reference to the head of our linked list 
          self.head = None
          # reference to the tail of our linked list 
          self.tail = None
  ​
      def enqueue(self, val):
          new_node = Node(val)
          # check if our queue is empty 
          if self.head is None and self.tail is None:
              self.head = new_node  
              self.tail = new_node
          # adds the val to one of the queue 
          else:
              # connect the old tail to the new node 
              self.tail.next = new_node
              # update the tail reference to refer to 
              # the new node 
              self.tail = new_node
  ​
      def dequeue(self):
          # check if the our queue is empty
          if self.head is None and self.tail is None:
              return None
          # check is the queue only has one element
          if self.head == self.tail:
              old_head = self.head
              self.head = None
              self.tail = None
              return old_head.val
          # removes a val from the opposite end 
          # in which the element was added 
          else:
              old_head = self.head 
              self.head = self.head.next
              return old_head.val
      
  queue = Queue()
  ​
  queue.enqueue(15)
  queue.enqueue(22)
  queue.enqueue(27)
  ​
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  Co

2. STACK USING LL:

  class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
​
# Inplement a Stack using a linked list 
  class Stack:
      def __init__(self):
          # ref to the head node of our linked list 
          self.head = None 
  ​
      def push(self, val):
          # adds the val as the new head
          # of our linked list 
          
          new_node = Node(val)
          # connect the new node to the current head 
          new_node.next = self.head
          # set the head reference to refer to the
          # new node 
          self.head = new_node
  ​
      def pop(self):
          # check if the stack is empty
          if not self.head:
              # this is an empty stack 
              return None
          # take another reference to the current head 
          old_head = self.head
          # returns the value stored at the head
          # and moves the head reference to the 
          # next linked list node 
          self.head = self.head.next
          
          return old_head.val
  ​
  stack = Stack()
  ​
  stack.push(11)
  stack.push(14)
  stack.push(15)
  ​
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())


3. MAX STACK:

    """
  You've encountered a situation where you want to easily be able to pull the
  largest integer from a stack.
  ​
  You already have a `Stack` class that you've implemented using a dynamic array.
  ​
  Use this `Stack` class to implement a new class `MaxStack` with a method
  `get_max()` that returns the largest element in the stack. `get_max()` should
  not remove the item.
  ​
  *Note: Your stacks will contain only integers. You should be able to get a
  runtime of O(1) for push(), pop(), and get_max().*
  """
  class Stack:
      def __init__(self):
          """Initialize an empty stack"""
          self.items = []
  ​
      def __len__(self):
          return len(self.items)
  ​
      def push(self, item):
          """Push a new item onto the stack"""
          self.items.append(item)
  ​
      def pop(self):
          """Remove and return the last item"""
          # If the stack is empty, return None
          # (it would also be reasonable to throw an exception)
          if not self.items:
              return None
  ​
          return self.items.pop()
  ​
      def peek(self):
          """Return the last item without removing it"""
          if not self.items:
              return None
          return self.items[-1]
  ​
  class MaxStack:
      def __init__(self):
          # Your code here
          self.stack = Stack()
          self.maxes = Stack()
  ​
      def push(self, item):
          """Add a new item onto the top of our stack."""
          # Your code here
          self.stack.push(item)
          # check to see if our input > our current max 
          if len(self.maxes) == 0 or item > self.maxes.peek():
              self.maxes.push(item)
  ​
      def pop(self):
          """Remove and return the top item from our stack."""
          # Your code here
          # check our maxes stack to see if the element we're 
          # popping == the current max 
          if len(self.stack) == 0:
              return None
  ​
          if self.stack.peek() == self.maxes.peek():
              self.maxes.pop()
  ​
          return self.stack.pop()
  ​
      def get_max(self):
          """The last item in maxes_stack is the max item in our stack."""
          # Your code here
          """
          Idea 1: Iterate through all of the elements in our stack, find the 
          largest, and return it. O(n) 
  ​
          Idea 2: Can we make a `self.max` property in the class and 
          modify it as we go? O(1)
          What happens when we pop the max value from our stack? How 
          do we find the next max value that needs to replace it? 
          It's not enough to just store the current max. What we need 
          is the history of all the maxes. This way, when we remove the 
          current max, we know what was the max before it, and we can 
          set that as our current max.
          We'll use another stack specifically to keep track of the 
          history of max values.
          """
          return self.maxes.peek()
  ​
  max_stack = MaxStack()
  print(max_stack.get_max()) # returns None
  ​
  max_stack.push(15)
  print(max_stack.get_max()) # returns 15
  ​
  max_stack.push(100)
  print(max_stack.get_max()) # returns 100
  ​
  max_stack.push(22)
  print(max_stack.get_max()) # returns 100
  ​
  print(max_stack.pop()) # returns 22 
  print(max_stack.get_max()) # returns 100
  ​
  print(max_stack.pop()) # returns 100
  print(max_stack.get_max()) # returns 15


4. QUE USING TWO STACKS:

    """
  Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
  should have an `enqueue()` method and a `dequeue()` method that ensures a
  "first in first out" (FIFO) order.
  ​
  As you write your methods, you should optimize for time on the `enqueue()` and
  `dequeue()` method calls.
  ​
  The Stack class that you will use has been provided to you.
  """
  class Stack:
      def __init__(self):
          self.data = []
  ​
      # method to get the length the stack 
      def __len__(self):
          return len(self.data)
          
      def push(self, item):
          self.data.append(item)
  ​
      def pop(self):
          if len(self.data) > 0:
              return self.data.pop()  # O(1)
          return "The stack is empty"
  ​
  class QueueTwoStacks:
      def __init__(self):
          # holds the elements from the in_stack in reversed order 
          # when we call the dequeue method, we'll pop from this stack 
          self.out_stack = Stack()
          # holds the incomine enqueued elements 
          self.in_stack = Stack()
  ​
      def enqueue(self, item):
          # add the element to our `in_stack` 
          self.in_stack.push(item)
  ​
      def dequeue(self):
          # we need to check if the `out_stack` is empty 
          # otherwise, just pop from the top of the `out_stack` 
          if len(self.out_stack) == 0:
              # empty the contents of the `in_stack` into the `out_stack` 
              while len(self.in_stack) != 0:
                  # pop from the in_stack
                  popped = self.in_stack.pop()
                  # add it to the out_stack 
                  self.out_stack.push(popped)
          
          return self.out_stack.pop()
  ​
  q = QueueTwoStacks()
  ​
  print(q.dequeue())
  ​
  q.enqueue(3)
  q.enqueue(6)
  print(q.dequeue())
  q.enqueue(7)
  q.enqueue(8)
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())