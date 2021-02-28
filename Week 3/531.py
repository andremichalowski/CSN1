
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

2. TIME AND SPACE COMPLEXITY, STRENGTHS AND WEAKNESSES, COMMON USES:

  A. TIME AND SPACE COMPLEXITY:
    TC: Time Complexity:
      + Most time complexity depends on the balance of tree: # This is the same for insert and delete
        - Balanced: O(log_n) 
        - Unbalanced: O(n)
    SC: Space Complexity:
      + O(n) Linear #Each node in BST will take up space in memory

  B. STRENGTHS AND WEAKNESSES
    1. STRENGTHS:
      1. Sorted by default # you can pull data in-order traversal
      2. Efficient Searches # O(log n)
        # Same efficiency as sorted Array
          # faster with insertion and deletion though
        # Slower than dictionaries in best case
          # faster than dictionaries in worst case
    2. WEAKNESSES:
      1. Unbalanced trees are more inefficient 
      2. Not especially efficient in anything Specific #(Even though good at general purpose efficiency)

3. CONSTRUCT A BINARY SEARCH TREE THAT CAN PERFORM BASIC OPERATIONS WITH A LOGARITHMIC TIME COMPLEXITY:
  1. Node class:
    class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

  2. BST CLASS:
    class BST:
      def __init__(self, value):
          self.root = BSTNode(value)

      def insert(self, value):
          self.root.insert(value)

      def search(self, value):
          self.root.search(value)
