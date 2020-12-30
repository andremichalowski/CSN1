1. TREE TRAVERSAL TYPES:

  # 1. DEPTH FIRST: 
  #   A. InOrder
  #   B. PreOrder
  #   C. PostOrder
  # 2. BREADTH FIRST


  1. DEPTH FIRST (INORDER):

    Go to the left subtree
    Visit node
    Go to the right subtree

    class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)
        res.append(root.val)
        helper(root.right, res)

    def inorder_traversal(root):
        result = []
        helper(root, result)
        return result


  2. DEPTH FIRST (PREORDER):

    Visit the node
    Go to the left subtree
    Go to the right subtree

    class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def helper(root, res):
        if root is None:
            return
        res.append(root.val)
        helper(root.left, res)
        helper(root.right, res)

    def preorder_traversal(root):
        result = []
        helper(root, result)
        return result

