1. SHORTEST PATH: What type of search usually returns the shortest path from the starting vertext to the target vertex once the target is found?
    >>>>> Breadth First Search (Because it never visits a node twice (basically))

2. BFS DATA STRUCTURE FIFO:
  >>>>> Queue is best for BFS FIFO functioning.

3. METHOD THAT VISITS EVERY NODE IN GRAPH:
  >>>>> DFS (Depth First Search)

4. FRIEND CIRCLES:
  There are N students in a baking class together. Some of them are friends, while some are not friends. The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students who are either direct or indirect friends.

  Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

  You need to write a function that can output the total number of friend circles among all the students.

    seen = set()
    def dfs(i):
        for j in range(len(friendships[0])):
            if friendships[i][j] and j not in seen:
                seen.add(j)
                dfs(j)
    
    return sum(dfs(i) or 1 for i in range(len(friendships)) if i not in seen)