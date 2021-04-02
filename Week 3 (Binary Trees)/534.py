1. REPRESENT A BREADTH FIRST SEARCH OF A GRAPH IN PSUEDO CODE AND REVIEW TYPICAL APPLICATIONS FOR ITS USE:

BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
        queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]  // Peek at head of the queue, but do not dequeue!

        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)

        queue.dequeue()
        u.color = black

You can see that we start with a graph and the vertex we will start on. The very first thing we do is go through each of the vertices in the graph and mark them with the color white. At the outset, we mark all the verts as unvisited.

Next, we mark the starting vert as gray. We are exploring the starting verts’ neighbors. We also enqueue the starting vert, which means it will be the first vert we look at once we enter the while loop.

The condition we check at the outset of each while loop is if the queue is not empty. If it is not empty, we peek at the first item in the queue by storing it in a variable.

Then, we loop through each of that vert's neighbors and:

We check if it is unvisited (the color white).
If it is unvisited, we mark it as gray (meaning we will explore its neighbors).
We enqueue the vert.
Next, we dequeue the current vert we've been exploring and mark that vert as black (marking it as visited).

We continue with this process until we have explored all the verts in the graph.


2. REPRESENT A DEPTH FIRST SEARCH (DFS) OF A GRAPH IN PSUEDO CODE AND REVIEW TYPICAL APPLICATIONS FOR ITS USE:

DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black


You can see that we have two functions in our pseudo-code above. The first function, DFS() takes the graph as a parameter and marks all the verts as unvisited (white). It also sets the parent of each vert to null. The next loop in this function visits each vert in the graph, and if it is unvisited, it passes that vert into our second function DFS_visit().

DFS_visit() starts by marking the vert as gray (in the process of being explored). Then, it loops through all of its unvisited neighbors. In that loop, it sets the parent and then makes a recursive call to the DFS_visit(). Once it's done exploring all the neighbors, it marks the vert as black (visited).


3. IMPLEMENT A BREADTH FIRST SEARCH:

 Previously used "Vertex Class" and "Graph Class" (GC w/added BFS)


 1. Vertex:
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


    2. Graph (w/Breadth First Search):

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

    def breadth_first_search(self, starting_vert):
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vert)
        visited.add(starting_vert)
        while to_visit.size() > 0:
            current_vert = to_visit.dequeue()
            for next_vert in current_vert.get_connections():
                if next_vert not in visited:
                    visited.add(next_vert)
                    to_visit.enqueue(next_vert)


4. IMPLEMENTING A DEPTH FIRST SEARCH:

  Previously used "Vertex Class" and "Graph Class" (GC w/added DFS)

  1. Vertex:
    - (See above)
    
  2. Graph (With DFS added):
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

      def depth_first_search(self, vertex, visited = set()):
          visited.add(vertex)
          for next_vert in vertex.get_connections():
              if next_vert not in visited:
                  self.depth_first_search(next_vert, visited)