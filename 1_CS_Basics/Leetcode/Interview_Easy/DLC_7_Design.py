1. SHUFFLE AN ARRAY:

  class Solution:
      def __init__(self, nums):
          self.array = nums
          self.original = list(nums)

      def reset(self):
          self.array = self.original
          self.original = list(self.original)
          return self.array

      def shuffle(self):
          aux = list(self.array)

          for idx in range(len(self.array)):
              remove_idx = random.randrange(len(aux))
              self.array[idx] = aux.pop(remove_idx)

          return self.array

2. MIN STACK:
#https://mail.google.com/mail/u/0/#inbox?projector=1

  class MinStack:
      def __init__(self):
          self.my_stack = []

      def push(self, x):
          if self.my_stack == []:
              self.my_stack.append((x,x))
          else:
              minimum = self.my_stack[-1][1]
              self.my_stack.append((x, min(x, minimum)))

      def pop(self):
          return self.my_stack.pop()[0]
          
      def top(self):
          return self.my_stack[-1][0]

      def getMin(self):
          return self.my_stack[-1][1]