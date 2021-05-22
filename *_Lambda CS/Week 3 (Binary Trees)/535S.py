1. cs BST RANGE SUM:

https://leetcode.com/problems/range-sum-of-bst/solution/

You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# def csBSTRangeSum(root, lower, upper):
    # def dfs(root, ans):
    #     if root:
    #         if lower <= root.value <= upper:
    #             ans += root.value
    #         if lower < root.value:
    #             dfs(root.left)
    #         if root.value < upper:
    #             dfs(root.right)
    #     return ans

    # ans = 0
    # result = dfs(root, ans)
    # return result
    
# def csBSTRangeSum(root, lower, upper):
#     ans = 0
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node:
#             if lower <= node.value <= upper:
#                 ans += node.value
#             if lower < node.value:
#                 stack.append(node.left)
#             if node.value < upper:
#                 stack.append(node.right)
#     return ans

def csBSTRangeSum(root, lower, upper):
    if not root:
        return 0
    sum = 0
    if root.value > lower:
        sum += csBSTRangeSum(root.left, lower, upper)
    if root.value < upper:
        sum += csBSTRangeSum(root.right, lower, upper)
    if lower <= root.value <= upper:
        sum += root.value     
        
    return sum


2. EXPLANATION:

I used a Depth First Search to search for values that were within the range of the lower and upper bounds and then add those those values to an aggregator that was returned. It was difficult to decide on a recursive or iterative approach and how to implement aggregation in the case of a recursion. 

3. O OF N VALUE:

Time: O(N) #N = number of tree nodes
Space Complexity: O(N) 

These were essentially the most efficient methods. It may have been better to use a recursive solution because it would have been more terse code but it results in essentially the same space and efficiency. 

----

4. INVERT A BINARY TREE:
  Given a binary tree, write a function that inverts the tree.
  https://leetcode.com/problems/invert-binary-tree/

  #
  # Binary trees are already defined with this interface:
  # class Tree(object):
  #   def __init__(self, x):
  #     self.value = x
  #     self.left = None
  #     self.right = None
      
  def csBinaryTreeInvert(root):
      if root:
          root.left, root.right = (
              csBinaryTreeInvert(root.right), 
              csBinaryTreeInvert(root.left))
      return root

  5. EXPLANATION:

  The solution for this problem required taking what is left of the root and defining it as right and visa versa. No specific obstacles or difficulties. 


  6. COMPLEXITY:

  Time Complexity: O(n) 
  Space Complexity: O(n)

  Each node only has to be visited once so the relationship is direct. 

  Because elements of the height of the tree are O(n) this particular problem also has a space complexity of O(n).

  This problem was solved fairly efficiently I can't think of another way it could be solved more efficiently.


7. FIND ALL PATHS FROM A TO B:

  You are given a directed acyclic graph (DAG) that contains N nodes.

  Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

  graph[a] is a list of all nodes b for which the edge a -> b exists.

  def csFindAllPathsFromAToB(graph):
    class GraphNode:
        def __init__(self, value=None):
            self.value = value
            self.connections = []
        
    paths= []
    currentPath= [0]
    targetNode= len(graph)-1
    def helper(currentPath, index):
        if index==targetNode:
            paths.append(currentPath.copy())
            return
        for i in range(0, len(graph[index])):
            currentPath.append(graph[index][i])
            helper(currentPath, graph[index][i])
            currentPath.pop()
    helper(currentPath, 0)
    return paths


  8. EXPLANATION:

    
