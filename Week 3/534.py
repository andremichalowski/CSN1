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


