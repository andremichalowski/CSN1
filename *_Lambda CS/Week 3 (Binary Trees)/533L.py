Graphs Sean Chen December 16th: https://youtu.be/dGmzSp5N6HU

Repo: https://github.com/LambdaSchool/cs-guided-project-graphs-i


1. PRINT CONNECTIONS (OBJECT REPRESENTATION FOR A GRAPH):
  class GraphNode:
      def __init__(self, value=None):
          self.value = value 
          self.connections = [] 
  ​
  g1 = GraphNode()
  g2 = GraphNode()
  g3 = GraphNode()
  g4 = GraphNode()
  ​
  g1.connections.append(g2)
  g1.connections.append(g3)
  g1.connections.append(g4)
  ​
  directed_graph = [
      [1, 2], # Node 0 
      [3],    # Node 1 
      [3],    # Node 2 
      [4],    # Node 3 
      [],     # Node 4 
  ]
  ​
  def print_graph(graph):
      for node, connections in enumerate(graph):
          print(f'Graph Node {node} is connected to {connections}')

  print_graph(directed_graph)
  Collapse


2. LEGAL GRAPH COLORING:

  class GraphNode:
      def __init__(self, val):
          self.val = val
          self.neighbors = set()
          self.color = None
  ​
  colors = ['Red', 'Green', 'Yellow', 'Blue', 'Purple']
  ​
  def color_graph(graph, colors):
      for node in graph: 

          illegal_colors = set() # Set illegal colors and add them respectively based on neighbor colors
          for neighbor in node.neighbors: 
              if neighbor.color not in illegal_colors:
                  illegal_colors.add(neighbor.color)
  ​
          for color in colors: #Whatever color from color list that is not illegal add
              if color not in illegal_colors:
                  node.color = color 
                  break
  ​
  ​
  g1 = GraphNode('G1')
  g2 = GraphNode('G2')
  g3 = GraphNode('G3')
  g4 = GraphNode('G4')
  g5 = GraphNode('G5')
  ​
  g1.neighbors.add(g2)
  g1.neighbors.add(g4)
  g1.neighbors.add(g3)
  ​
  g2.neighbors.add(g1)
  g2.neighbors.add(g4)
  g2.neighbors.add(g5)
  ​
  g3.neighbors.add(g1)
  g3.neighbors.add(g5)
  g3.neighbors.add(g4)
  ​
  g4.neighbors.add(g1)
  g4.neighbors.add(g2)
  g4.neighbors.add(g3)
  g4.neighbors.add(g5)
  ​
  g5.neighbors.add(g2)
  g5.neighbors.add(g3)
  g5.neighbors.add(g4)
  ​
  graph = [g1, g2, g3, g4, g5]
  ​
  color_graph(graph, colors)
  ​
  for node in graph:
      print(node.color)


3. NUMBER OF ISLANDS:

from collections import deque
​
def numIslands(grid):

    num_islands = 0 
    rows = len(grid)
    cols = len(grid[0])

    for r, row in enumerate(grid):
        for c, loc in enumerate(row):
            if loc == '1':
                num_islands += 1
                # radiate out from this spot using a BFT 
                queue = deque()
                queue.append((r, c))
                grid[r][c] = '0'
                
                while len(queue) > 0:
                    current = queue.popleft()
                    curr_r, curr_c = current[0], current[1]
                    # check in all 4 cardinal directions make sure to check against whether our current spot is on the edge of our map check north 
                    if curr_r - 1 >= 0 and grid[curr_r-1][curr_c] == '1':
                        queue.append((curr_r-1, curr_c))
                        grid[curr_r-1][curr_c] = '0' #toggle this spot
​
                    if curr_r + 1 < rows and grid[curr_r+1][curr_c] == '1': # check south
                        queue.append((curr_r+1, curr_c))
                        grid[curr_r+1][curr_c] = '0'

                    if curr_c + 1 < cols and grid[curr_r][curr_c+1] == '1': # check east 
                        queue.append((curr_r, curr_c+1))
                        grid[curr_r][curr_c+1] = '0'

                    if curr_c - 1 >= 0 and grid[curr_r][curr_c-1] == '1': # check west
                        queue.append((curr_r, curr_c-1))
                        grid[curr_r][curr_c-1] = '0'
​
    return num_islands
​
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
​
print(numIslands(grid))