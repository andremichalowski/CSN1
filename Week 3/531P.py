1. NODES PERFECT BINARY TREE:
  A. HEIGHT:
    log_2(n + 1) = h 
  B. NODES:
    N = 2^h - 1 #where h is height of binary tree

2. WHAT IS ONE OF THE PRIMARY WEAKNESSES OF THE BINARY SEARCH TREE AS A DATA STRUCTURE?
  A. It has slower lookups than a sorted array

3. WHAT DOES THE PHRASE "in order successor" mean when talking about node in BST?
  A. The node that has the next highest value

4. BALANCED BINARY TREE:
https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
  # Binary trees are already defined with this interface:
  # class Tree(object):
  #   def __init__(self, x):
  #     self.value = x
  #     self.left = None
  #     self.right = None
  def height(root): 
        
      # base condition when binary tree is empty 
      if root is None: 
          return 0
      return max(height(root.left), height(root.right)) + 1
    
  # function to check if tree is height-balanced or not 
  def balancedBinaryTree(root): 
        
      # Base condition 
      if root is None: 
          return True
    
      # for left and right subtree height 
      lh = height(root.left) 
      rh = height(root.right) 
    
      # allowed values for (lh - rh) are 1, -1, 0 
      if (abs(lh - rh) <= 1) and balancedBinaryTree( 
      root.left) is True and balancedBinaryTree( root.right) is True: 
          return True
    
      # if we reach here means tree is not  
      # height-balanced tree 
      return False


5. MINIMUM DEPTH BINARY TREE:
https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
  def minimumDepthBinaryTree(root):

    if root is None: 
        return 0 
    if root.left is None and root.right is None: 
        return 1
    if root.left is None: 
        return minimumDepthBinaryTree(root.right)+1
    if root.right is None: 
        return minimumDepthBinaryTree(root.left) +1 
      
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right))+1