1. MAXIMUM DEPTH OF A BINARY TREE:

  def maxDepth(root):
    if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


2. IS VALID BST:

https://www.youtube.com/watch?v=MILxfAbIhrE

  class Node: 
    
      # Constructor to create a new node 
      def __init__(self, data): 
          self.data = data  
          self.left = None
          self.right = None
    
    
  # Returns true if the given tree is a binary search tree 
  # (efficient version) 
  def isBST(node): 
      return (isBSTUtil(node, INT_MIN, INT_MAX))
  # Retusn true if the given tree is a BST and its values 
  # >= min and <= max 
  def isBSTUtil(root, min, max): 
      # An empty tree is BST 
      if root is None: 
          return True
      # False if this root violates min/max constraint 
      if root.data <= min or root.data > max: 
          return False
      # Otherwise check the subtrees recursively 
      # tightening the min or max constraint 
      return (isBSTUtil(root.left, min, root.data) and #root left becomes root, -infinity becomes min, original root becomes max 
            isBSTUtil(root.right, root.data, max)) # root right becomes root, original root becomes min, and infinity becomes max