## Graph data structure in adjacent list with DFS & BFS traversal ##

from collections import deque

## implementing Queue from previous lesson for BFS algorithm
class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


class Graph:
    def __init__(self, adj_list):
        self.data = adj_list
        self.visited = [False] * len(self.data)
        self.count = 0
        self.components = [False] * len(self.data)
        
    ## Depth First Search Algo.
    def dfs(self, node):
        if self.visited[node]:
            return
        self.visited[node] = True
        
        self.components[node] = self.count 

        neighboor = self.data[node]
        for next in neighboor:
            self.dfs(next)
    
    ## Finding connected components and number of connected components
    def findComponent(self):
        for i in range(0, len(self.data)):
            if not self.visited[i]:
                self.count += 1
                self.dfs(i)
        return self.count, self.components       


    ## Breadth First Search Algo.
    def bfs(self, start, end):

        prev = self.solve(start)

        return self.reconstructPath(start, end, prev)


    def solve(self, start):
        queue = Queue()
        queue.enqueue(start)

        ## Could make a local visited list or use a global one but a local one will be implemented as it won't need a global one like DFS ##
        visited_local = [False] * len(self.data)
        visited_local[start] = True    

        prev = [None] * len(self.data)    
        while not queue.isEmpty():
            node = queue.dequeue()
            neighboors = self.data[node]
            for neighboor in neighboors:
                if not visited_local[neighboor]:
                    queue.enqueue(neighboor)
                    visited_local[neighboor] = True
                    prev[neighboor] = node
        return prev

    # Finding shortest path of an unweighted graph using BFS
    def reconstructPath(self, start, end, prev):

        path = []
        i = end
        while not prev[i] == None:
            i = prev[i]
            path.append(i)
        
        path.reverse()
        
        if path[0] == start:
            return path
        return []


graph = Graph([[1, 5],
               [0, 5, 2, 4],
               [1, 6, 3],
               [2, 4],
               [1, 3],
               [0, 1],
               [2]])



## Finding connected components
## print(graph.findComponent())
## This method returns 2 values (count of components, component id of each node(in order))


## Find shortest path from node 0 --> 6
print(graph.bfs(0, 6))




