
1. PROPERTIES OF A BINARY TREE AND OF "PERFECT TREE":

  A. WHAT A BINARY TREE MIGHT LOOK LIKE:
    class BinaryTreeNode:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None

  B. NODES NUMBER?:
    - Equal to the the number of all previous nodes + 1 (???Does this apply to all cases???)

  C. FORMULAS:

    1. HEIGHT:
      log_2(n + 1) = h    #Where n is the number of nodes in the level

    2. NODES:
      n = 2^h - 1

