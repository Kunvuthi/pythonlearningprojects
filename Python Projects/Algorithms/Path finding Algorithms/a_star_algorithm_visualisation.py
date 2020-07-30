import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))   
pygame.display.set_caption("A* Path Finding Algorithm")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Lime = (0,255,0)
Blue = (65,105,225)
Yellow = (255,255,0)
Aqua = (0,255,255)
Endcolor = (139,0,139)
Grey = (128,128,128)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = White
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows


    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == Red

    def is_open(self):
        return self.color == Lime

    def is_barrier(self):
        return self.color == Black

    def is_start(self):
        return self.color == Yellow

    def is_end(self):
        return self.color == Endcolor

    def reset(self):
        self.color = White

    def make_open(self):
        self.color = Lime

    def make_start(self):
        self.color = Yellow

    def make_barrier(self):
        self.color = Black 

    def make_end(self):
        self.color == Endcolor

    def make_path(self):
        self.color == Blue 

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows 
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows 
    for i in range(rows):
        pygame.draw.line(win, Grey, (0,i*gap), (width,i*gap))
        for j in range(rows):
            pygame.draw.line(win, Grey, (j*gap,0), (j*gap,width))

def draw(win, grid, rows, width):
    win.fill(White)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows 
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  ## Left Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()
                     

            elif pygame.mouse.get_pressed()[2]:  ## Right Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None

                elif spot == end:
                    end == None
    pygame.quit()


main(WIN, WIDTH)

# class Graph:
#     def __init__(self, arr):
#         self.data = arr 
#         self.num_nodes = len(self.data)


#     def dijkstra(self, start): ## if want to find shortest distance with better performance, look at the bottom's comment!
#         vis = [False] * self.num_nodes
#         prev = [None] * self.num_nodes
#         dist = [inf] * self.num_nodes
#         dist[0] = 0

#         ## Implementing a Priority Queue  ##
#         pq = PriorityQueue()
#         pq.put((start, 0))
#         while not pq.empty():
#             index, MinDist = pq.get()
#             vis[index] = True

#             ## Optimising to ignore distance that is smaller than the current distance in dist array
#             if dist[index] < MinDist:
#                 continue
#             for edge in self.data[index]:
#                 ## if node is already visited then continue ##
#                 if vis[edge[0]]:
#                     continue

#                 new_dist = dist[index] + edge[1]

#                 if new_dist < dist[edge[0]]:
#                     prev[edge[0]] = index
#                     dist[edge[0]] = new_dist
#                     pq.put((edge[0], new_dist))
#             # if index == end_:
#             #     return dist[end]           
#         return (dist, prev)