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



3. IS SYMETRIC:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    def isSymmetric(self, root):
        if root is None:
          return True
        else:
          return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
          return True
        if left is None or right is None:
          return False

        if left.val == right.val:
          outPair = self.isMirror(left.left, right.right)
          inPiar = self.isMirror(left.right, right.left)
          return outPair and inPiar
        else:
          return False

    def isSymetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False


4. BINARY TREE LEVEL ORDER TRAVERSAL:

def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

5. CONVERT SORTED ARRAY TO (HEIGHT BALANCED) BINARY SEARCH TREE:

     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root