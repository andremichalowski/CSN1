1. BST Basic INSERT AND SEARCH:
  class BSTNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 
​
    def insert(self, value):        
        # if we don't want to allow duplicates
        # if value == self.value:
        #     return 
        if value < self.value:
            if self.left is not None: # we need to recurse in the left direction 
                self.left.insert(value)
            else: # there's no node in the direction we need to go in
                self.left = BSTNode(value) # we can park the value in that spot 
        else: # go right # check if there is a child node in the right direction 
            if self.right is not None:
                self.right.insert(value) # there's a node in the direction we need to go in 
            else:  # there's no node in the direction we need to go in 
                self.right = BSTNode(value) # we can park the value in that spot 

2. FIND MAX DEPTH OF BINARY TREE:

  def maxDepth(root):
      if root is None:
          return 0 
  ​     
      left_depth = maxDepth(root.left) # the root node is not empty recurse on the left and right sides to find their respective depths 
      right_depth = maxDepth(root.right)
  ​
    answer = max(left_depth, right_depth) + 1 # add 1 to account for this current node
      return answer
  ​
  # Creating the binary tree in the above example

  # left = BinaryTreeNode(12)
  # right = BinaryTreeNode(32, BinaryTreeNode(8), BinaryTreeNode(4))
  # root = BinaryTreeNode(5, left, right)
  # ​
  # print(maxDepth(root))

3. VALID (PERFECT) BINARY TREE CHECK:

  class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
​
  # is this function expecting an answer? 
  def is_valid_BST(root):
      # Your code here
      # keep track of the valid range as we're traversing down the tree 
      # when we go left, limit the upper bound to be root - 1 
      # when we go right, limit the lower bound to be root + 1 
      # check if the current node's value falls within the range
      # check the root's left child
          # if the left's child value >= root's value 
              # return False
      # check the root's right child 
          # if the right's child value <= root's value 
              # return False 
      # otherwise, return True 
      return recurse(root, float('-inf'), float('inf'))
  ​
  def recurse(root, min_bound, max_bound):
      # base case(s) 
      # check the current value against the range 
      # we've traversed the whole tree and never saw a False, so return True 
      if root is None:
          return True
      # if the current value falls outside the range, return False 
      if root.value < min_bound or root.value > max_bound:
          return False 
      # how do we get closer to our base case? 
      # recurse with the left child and update the range 
      left = recurse(root.left, min_bound, root.value - 1)
      # recurse with the right child and update the range 
      right = recurse(root.right, root.value + 1, max_bound)
  ​
      # if either left or right is False, return False 
      return left and right


  Here's a working implementation of the is_valid_bst problem.
  One important thing to realize with this problem is that it isn't enough to just recursively check each node to make sure its left child's value is less than the root's value and that the right child's value is greater than the root's value. Just doing that will return the wrong answer for input such as this:
      10
    /  \
    2    8
        / \
      6  12
  In this case, 6 is less than 8 and 12 is greater than 8, but this isn't a valid binary search tree since 6 should not be on the right side of the root node 10.
  To address this, we'll need to keep track of the "valid range" that each node can have. In the case of the node 6 in the above example, its valid range is > 8 but < 10. Since 6 doesn't fall in that range, we return False.
  As far as how to implement that recursively, we create another function that performs the recursion itself, since we need to keep track of the valid range for each node on each recursive call. This means that we need to pass the min and max bounds into each recursive call. However, since the is_valid_BST function's signature doesn't allow us to do that, we can get around this by defining a new function with the signature we need.
  So the base case here is when we either see that the current value in a node is not contained within its valid range, in which case we return false, or when we traverse all the way down to a leaf node and didn't encounter any problems, at which point we return true for the current path we traversed down. At the end of the traversal, if no paths return false, then the entire tree is valid.