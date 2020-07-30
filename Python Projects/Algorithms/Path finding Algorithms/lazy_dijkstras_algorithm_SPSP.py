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


    def dijkstra(self, start): ## if want to find shortest distance with better performance, look at the bottom's comment!
        vis = [False] * self.num_nodes
        prev = [None] * self.num_nodes
        dist = [inf] * self.num_nodes
        dist[0] = 0

        ## Implementing a Priority Queue  ##
        pq = PriorityQueue()
        pq.put((start, 0))
        while not pq.empty():
            index, MinDist = pq.get()
            vis[index] = True

            ## Optimising to ignore distance that is smaller than the current distance in dist array
            if dist[index] < MinDist:
                continue
            for edge in self.data[index]:
                ## if node is already visited then continue ##
                if vis[edge[0]]:
                    continue

                new_dist = dist[index] + edge[1]

                if new_dist < dist[edge[0]]:
                    prev[edge[0]] = index
                    dist[edge[0]] = new_dist
                    pq.put((edge[0], new_dist))
            # if index == end_:
            #     return dist[end]           
        return (dist, prev)

    def shortest_path_using_dijk(self, start, end):
        dist, prev = self.dijkstra(start)
        path = []
        at = end
        ## finding whether end node is reachable, otherwise, stop and return nothing.
        if dist[end] == inf:
            return path
        while prev[at]:
            at = prev[at]
            path.append(at)
        path.reverse()
        return path
        
## Keep in mind that this implementation will find ALL the shortest distance from the start node first before finding the shortest path from start node to end node ##
## If you only wanted to find the distance for neccessary path to get to the end node which may increase the speed of this program, you can put a condition outside of the for loop ##
## checking if index == end, then stop and return dist[end].   ## 
## Also don't forget to pass a parameter change and argument of 'end' in dijkstra() method ##

arr = [[(1,7)],
       [(2,5),(3,2),(5,10)],
       [(4,6)],
       [(6,7)],
       [(5,3), (7,5)],
       [(7,2), (8,4)],
       [(5,5)],
       [(8,5)],
       [(9,1)],
       [(8,4)]]
    
g = Graph(arr)
print(g.shortest_path_using_dijk(0,9))
print(g.dijkstra(0))