1. MAXIMUM DEPTH OF A BINARY TREE:

  def maxDepth(root):
    if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))