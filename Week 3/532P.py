1. TWO PRIMARY CATEGORIES FOR TREE TRAVERSAL:
  1. Depth first
  2. Breadth first

2. THREE DEPTH TRAVERSAL TYPES:
  1. InOrder
  2. PreOrder
  2. PostOrder

3. INORDER STEPS:
  1. Go to left sub-tree:
  2. Visit node
  3. Go to right sub-tree:

4. PREORDER STEPS:
  1. Visit node
  2. Go to left sub-tree:
  3. Go to right sub-tree:

5. POSTORDER STEPS:
  1. Go to left sub-tree:
  2. Go to right sub-tree:
  3. Visit node

6. DATA STRUCTURE USED FOR ITERATIVE TRAVERSAL:
  1. stack

7. IN ORDER TREE TRAVERSAL:
  You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

  # Binary trees are already defined with this interface:
  # class Tree(object):
  #   def __init__(self, x):
  #     self.value = x
  #     self.left = None
  #     self.right = None
  def binaryTreeInOrderTraversal(root):
      # def helper(root, res):
      #     if root is None:
      #         return
      #     helper(root.left, res)
      #     res.append(root.value)
      #     helper(root.right, res)

      # def inorder_traversal(root):
      #     result = []
      #     helper(root, result)
      #     return result

8. ITERATIVE TREE TRAVERSAL: #SAME TREE AS #7

# Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

# Given a binary tree of integers t, return its node values in the following format:

# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
# Etc.


  # Binary trees are already defined with this interface:
  # class Tree(object):
  #   def __init__(self, x):
  #     self.value = x
  #     self.left = None
  #     self.right = None

  from collections import deque 

  def traverseTree(root):
        queue = deque()
        result = []
        queue.append(root)
        
        while len(queue) > 0:
            current = queue.popleft()
            result.append(current.value)
            
            if current.left is not None:
                queue.append(current.left)
                
            if current.right is not None:
                queue.append(current.right)
                
        return result 

9. PREORDER BST TRAVERSAL (SAVING PATH HISTORY):

Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).


  # Binary trees are already defined with this interface:
  # class Tree(object):
  #   def __init__(self, x):
  #     self.value = x
  #     self.left = None
  #     self.right = None
  def treePaths(root):
      def helper(root, res, curr_path = []):
          if root is None:
              return
          
          curr_path.append(str(root.value))
          
          if root.right is None and root.left is None: 
              res.append("->".join(curr_path))
              
          helper(root.left, res, curr_path)
          helper(root.right, res, curr_path)
      
      result = []
      helper(root, result)
      return result