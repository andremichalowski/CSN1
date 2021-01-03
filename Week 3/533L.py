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


