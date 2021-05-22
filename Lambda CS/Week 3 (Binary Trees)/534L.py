1. FIND ALL PATHS IN A BT (REVIEW):

  def treePaths(root):
      result = [] 
      dft(root, [], result)
      
      return result 

  def dft(node, current_path, result):
      if not node:
          return
  
      current_path.append(f'{node.value}')
      
      if is_leaf(node):
          result.append("->".join(current_path[:]))

      dft(node.left, current_path, result)
      dft(node.right, current_path, result)

      current_path.pop()
      
  def is_leaf(node):
      return node.left is None and node.right is None


2. FIND ALL PATHS IN A GRAPH:

  def csFindAllPathsFromAToB(graph):
      result = [] 
      dft(graph, 0, [0], result)
      return result 
      
  def dft(graph, current_node, current_path, result):
      if current_node == len(graph) - 1:
          result.append(current_path[:])
      connections = graph[current_node]
      
      for connection in connections:
          current_path.append(connection)
          dft(graph, connection, current_path, result)
          current_path.pop()


3. FLOOD FILL:


def flood_fill(image, sr, sc, new_color):
    starting_color = image[sr][sc]
    bft(image, starting_color, new_color, sr, sc)
    return image 
​
from collections import deque
​
def bft(image, starting_color, new_color, r, c):
    rows = len(image)
    cols = len(image[0])
​
    queue = deque()
    queue.append((r, c)) 
    
    while len(queue) > 0:
        curr_r, curr_c = queue.popleft()
        image[curr_r][curr_c] = new_color
​
        # north 
        if curr_r - 1 >= 0 and image[curr_r-1][curr_c] == starting_color:
            queue.append((curr_r-1, curr_c))
        # south 
        if curr_r + 1 < rows and image[curr_r+1][curr_c] == starting_color:
            queue.append((curr_r+1, curr_c))
        # east 
        if curr_c + 1 < cols and image[curr_r][curr_c+1] == starting_color:
            queue.append((curr_r, curr_c+1))
        # west 
        if curr_c - 1 >= 0 and image[curr_r][curr_c-1] == starting_color:
            queue.append((curr_r, curr_c-1))
​
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
​
print(flood_fill(image, 1, 1, 2))