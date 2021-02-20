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
  def isBSTUtil(node, mini, maxi): 
        
      # An empty tree is BST 
      if node is None: 
          return True
    
      # False if this node violates min/max constraint 
      if node.data < mini or node.data > maxi: 
          return False
    
      # Otherwise check the subtrees recursively 
      # tightening the min or max constraint 
      return (isBSTUtil(node.left, mini, node.data -1) and
            isBSTUtil(node.right, node.data+1, maxi)) 