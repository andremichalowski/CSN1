1. MAXIMUM DEPTH OF A BINARY TREE:

  def maxDepth(root):
    if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


2. IS VALID BST:

  def isValidBST(self, root: TreeNode) -> bool:
    def inorder(root):
                if not root:
                    return True
                if not inorder(root.left):
                    return False
                if root.val <= self.prev:
                    return False
                self.prev = root.val
                return inorder(root.right)

            self.prev = -math.inf
            return inorder(root)
