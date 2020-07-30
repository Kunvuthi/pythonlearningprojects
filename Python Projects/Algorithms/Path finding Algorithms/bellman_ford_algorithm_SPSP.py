
from math import inf

class Graph:
    def __init__(self, arr):
        self.data = arr 
        self.num_nodes = len(self.data)


    def bellman(self, start): 
        dist = [inf] * self.num_nodes
        dist[start] = 0    
            
        for i in range(self.num_nodes-1):            
            for edge in self.data[i]:
                new_dist = dist[i] + edge[1]
                ## Relaxing the edge
                if new_dist < dist[edge[0]]:
                    dist[edge[0]] = new_dist

        ## Run the algorithm one more time to ##
        ## find the value that is caught in a negative cycle ##
        ## it is quite optional               ##
        for i in range(self.num_nodes):
            for edge in self.data[i]:
                new_dist = dist[i] + edge[1]
                if new_dist < dist[edge[0]]:
                    dist[edge[0]] = -inf
        return dist

## Note: the context is Index[(a,b),(c,d)] where Index is the Node number; (a,b) are (node_to, cost_to_that_node) ##
## No negative cycle graph representation ## 
arr = [[(1,5),(2,4)],
       [(2,-2),(3,-1)],
       [(4,3)],
       [(5,2)],
       [(3,6)],
       [(4,4)]]

g = Graph(arr)

## Eg. of Negative Cycle ## execute the program to see
arr2 = [[(1,5),(2,4)],
       [(2,-2),(3,-1)],
       [(4,3)],
       [(5,2)],
       [(1,-2),(3,6)],
       [(4,4)]]

g2 = Graph(arr2)

print(g.bellman(0))
print(g2.bellman(0))