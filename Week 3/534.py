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


