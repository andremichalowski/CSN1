
1. GRAPHS AND TREES RELATIONSHIPS:
  - Which of the following statements is true?
   >>>> All trees are graphs but not all graphs are trees.


2. DIRECTED VERSUS UNDIRECTED GRAPHS:
  - Choose answer that best describes difference between directed and undirected graph. 
  >>>> Directed graphs best represent relationships that can be described as "mutual exchanges", while undirected graphs best represent relationships that can be described as, "one way".

3. GRAPH ADJACENCY LIST REPRESENTATION:
  - Choose the python code that correctly represents the graph shown in the picture using an adjacency list. 
  >>>>> (An adjacency list that accurately describes the picture... (See Screenshot))

4. GRAPH REPRESENTATION IN PYTHON INTERPRETER:
  - select python code written in an interactive interpreter that would correctly create the graph pictured)
  >>>>> (See screenshot)

5. FIND ALL PATHS FROM A TO B:
  - You are given a directed acyclic graph (DAG) that contains N nodes.
  Write a fxn that can find all the possible paths from node 0 to node N-1. You can return the path in any order.
  graph[a] is a list of all nodes b for which the edge a -> b exists.

  # directed_graph = [
  #     [1, 2],
  #     [3],
  #     [3],
  #     [4],
  #     []
  # ]


  def csFindAllPathsFromAToB( graph ):
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
