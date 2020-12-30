1. DEPTH FIRST TRAVERSAL ITERATIVELY: (NON RECURSIVE METHOD) (PREORDER STYLE?):

  def iter_dft(root):
      stack = [] 
      result = [] 

      stack.append(root)


      while len(stack) > 0:
          current = stack.pop() # pop off the top stack element this is the current node we're visiting 
  ​
          if current.right is not None: # add the current node's children to the stack (if it has children) 
              stack.append(current.right)
          if current.left is not None:
              stack.append(current.left)
  ​
          result.append(current.value)
  ​
      return result 
      
  from collections import deque 
  ​
  def bft(root):
      # visits the nodes of the tree in breadth-first order 
      # adds all the nodes to a result list and returns it 
      queue = deque() # holds on to nodes 
      result = [] # holds on to values of nodes 
  ​
      queue.append(root)
  ​
      while len(queue) > 0: 
          # dequeue the node that was added earliest to the queue 
          # current = queue.pop(0) # O(n)
          current = queue.popleft() # O(1) 
          # Ring buffer 
  ​
          result.append(current.value)
  ​
          if current.left is not None:
              queue.append(current.left)
  ​
          if current.right is not None:
              queue.append(current.right)
  ​
      return result 
