
1. WHAT IS A GRAPH, ITS COMPONENTS, AND USEFULL APPLICATIONS:

  https://lambdaschool.instructure.com/courses/582/pages/objective-01-describe-what-a-graph-is-explain-its-components-provide-examples-of-its-useful-applications-and-draw-each-of-the-different-graph-types?module_item_id=527099

  A. TYPES:

    1. DIRECTED AND UNDIRECTED:
      A. Directed:
        - uni-directional
        - bi-directional
      B. Undirected:
        - no-direction

    2. CYCLIC AND ACYCLIC:
      A. Cyclic:
        - able to re-visit a vert #undirected is cyclic
      B. Acyclic:
        - not able to revisit verts 

    3. WEIGHTED:
      A. Weighted:
        - some edges have different weights

    4. DIRECTED ACYCLIC GRAPHS (DAG'S):



2. ADJACENCY LIST + ADJACENCY MATRIX:

    A. GRAPH REPRESENTATIONS:
      1. Adjacency GRAPH
      2. Adjacency LIST
      3. Adjacency MATRIX


      1. ADJACENCY GRAPH:
        - Visual representation of vertices using shapes and arrows (see link)

      2, ADJACENCY LIST:
        - Dictionary that holds a list of vertices connected verteces. 
        class Graph:
          def __init__(self):
              self.vertices = {
                                  "A": {"B"},
                                  "B": {"C", "D"},
                                  "C": {"E"},
                                  "D": {"F", "G"},
                                  "E": {"C"},
                                  "F": {"C"},
                                  "G": {"A", "F"}
                              }

      3. ADJACENCY MATRIX:
        - Two dimensional array, a list of lists.
        class Graph:
          def __init__(self):
              self.edges = [[0,1,0,0,0,0,0],
                            [0,0,1,1,0,0,0],
                            [0,0,0,0,1,0,0],
                            [0,0,0,0,0,1,1],
                            [0,0,1,0,0,0,0],
                            [0,0,1,0,0,0,0],
                            [1,0,0,0,0,1,0]]


    B. TRADEOFFS:

      Shorthand	Property
        V	Total number of vertices in the graph
        E	Total number of edges in the graph
        e	Average number of edges per vertex

      
      Type	  Space	  Add-Vert	Remove-Vert	 Add-Edge	 Remove-Edge	Find-Edge	  Get-All-Edges
      List	  O(V+E)	O(1)	    O(V)	       O(1)	     O(1)	        O(1)	      O(1)
      Matrix	O(V^2)	O(V)	    O(V^2)	     O(1)	     O(1)	        O(1)	      O(V)

    
    C. WEIGHTS EXAMPLES:

      1. LIST:
        class Graph:
          def __init__(self):
              self.vertices = {
                                  "A": {"B": 1},
                                  "B": {"C": 3, "D": 2},
                                  "C": {},
                                  "D": {},
                                  "E": {"D": 1}
                              }

      2. MATRIX:
        class Graph:
          def __init__(self):
              self.edges = [[0,1,0,0,0],
                            [0,0,3,2,0],
                            [0,0,0,0,0],
                            [0,0,0,0,0],
                            [0,0,0,1,0]]


3. IMPLEMENT USER DEFINED VERTEX AND GRAPH CLASSES THAT ALLOW BASIC OPERATIONS:

  Vertex Class:

    class Vertex:
      def __init__(self, value):
          self.value = value
          self.connections = {}

      def __str__(self):
          return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

      def add_connection(self, vert, weight = 0):
          self.connections[vert] = weight

      def get_connections(self):
          return self.connections.keys()

      def get_value(self):
          return self.value

      def get_weight(self, vert):
          return self.connections[vert]

  Graph Class: 

    class Graph:
      def __init__(self):
          self.vertices = {}
          self.count = 0

      def __contains__(self, vert):
          return vert in self.vertices

      def __iter__(self):
          return iter(self.vertices.values())

      def add_vertex(self, value):
          self.count += 1
          new_vert = Vertex(value)
          self.vertices[value] = new_vert
          return new_vert

      def add_edge(self, v1, v2, weight = 0):
          if v1 not in self.vertices:
              self.add_vertex(v1)
          if v2 not in self.vertices:
              self.add_vertex(v2)
          self.vertices[v1].add_connection(self.vertices[v2], weight)

      def get_vertices(self):
          return self.vertices.keys()
 
