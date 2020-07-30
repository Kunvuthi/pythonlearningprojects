from math import inf
import numpy as np

class Graph:
    def __init__(self, arr):
        self.data = arr
        self.length = len(self.data)
        self.dp = [[0]*self.length]*self.length
        self.next = [[None]*self.length]*self.length

    def floydwarshall(self):
        self.setup(self.data)

        for k in range(self.length):
            for i in range(self.length):    
                for j in range(self.length):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
                        self.next[i][j] = self.next[i][k] 

        self.propagateNegativeCycles()
        return self.dp           

    def propagateNegativeCycles(self):

        for k in range(self.length):
            for i in range(self.length):    
                for j in range(self.length):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = -inf
                        self.next[i][j] = -1
        


    def setup(self, m):       
        for i in range(self.length):
            for j in range(self.length):
                self.dp[i][j] = m[i][j]
                if m[i][j] != inf:  
                    self.next[i][j] = j


arr = [[  0,   7,  inf,    5,  inf],
       [inf,   0,    2,  inf,  1],
       [inf, inf,    0,  inf,  inf],
       [inf, inf,  inf,    0,  -1],
       [  2,   3,  inf,  inf,  0]]

g = Graph(arr)
print(np.array(g.floydwarshall()))


        

    

        


