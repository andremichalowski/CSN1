1. TREE TRAVERSAL TYPES:

  !!! >>> https://lambdaschool.instructure.com/courses/582/pages/objective-01-recall-the-different-traversal-types-for-a-binary-tree-and-implement-a-function-to-complete-the-traversal-for-each-type?module_item_id=527102 
  
  # 1. DEPTH FIRST: 
  #   A. InOrder (L, N, R)
  #   B. PreOrder (N, L, R)
  #   C. PostOrder (L, R, N)
  # 2. BREADTH FIRST (Custom)


  1. DEPTH FIRST (INORDER) (Go Left, Visit Node, Go Right):

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

    # root = TreeNode(val=1, left=node_2, right=node_3)
    # root.left --> node with val 2

    # 1
    #  2
    #   4
    #    8
    #    -> 8
    #    ..
    #   -> 4
    #  -> 2
    #  5
    #   -> 5
    #   ..
    


  2. DEPTH FIRST (PREORDER) (Visit Node, Go Left, Go Right):

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


  3. DEPTH FIRST (POSTORDER) (Go Left, Go Right, Visit Node):

    Go to the left subtree
    Go to the right subtree
    Visit node

    class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)
        helper(root.right, res)
        res.append(root.val)

    def postorder_traversal(root):
        result = []
        helper(root, result)
        return result


  4. BREADTH FIRST (LEVEL ORDER) (See animation):

    class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def breadth_first_traversal(root):
        if root is None:
            return []

        result = []
        queue = []
        queue.append(root)

        while len(queue) != 0:
            node = queue.pop(0)
            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return result
