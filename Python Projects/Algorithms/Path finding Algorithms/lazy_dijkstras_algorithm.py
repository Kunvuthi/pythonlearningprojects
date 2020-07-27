## This algorithm is used in a non-negative weighted graph     ##
## We will be using an adjacency matrix to represent our graph ##
## Time complexity: average O(E*log(V))                        ##
## eg:                                                         ##
##                                   ##
##                                  ##
## Each Column represent the weight to each node, notice that there will be 0 across diagonally because weight from the node to itself should be 0 ##

from queue import PriorityQueue
from math import inf




class Graph:
    def __init__(self, arr):
        self.data = arr 
        self.num_nodes = len(self.data)


    def dijkstra(self, start):
        vis = [False] * self.num_nodes
        dist = [inf] * self.num_nodes
        dist[0] = 0

        ## Implementing a Priority Queue  ##
        pq = PriorityQueue()
        pq.put((start, 0))
        while not pq.empty():
            index, MinDist = pq.get()
            vis[index] = True
            if dist[index] < MinDist:
                continue
            for edge in self.data[index]:
                ## if node is already visited to ##
                if vis[edge[0]]:
                    continue

                new_dist = dist[index] + edge[1]

                if new_dist < dist[edge[0]]:
                    dist[edge[0]] = new_dist
                    pq.put((edge[0], new_dist))
        return dist


arr = [[(1,7)],
       [(2,5),(3,2),(5,10)],
       [(4,6)],
       [(6,7)],
       [(5,3), (7,5)],
       [(7,2), (8,4)],
       [(5,5)],
       [(8,5)],
       [(8,4)]]
    
g = Graph(arr)
print(g.dijkstra(0))