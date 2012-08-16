import random
import time
import pygame


pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((700,700))

grid = []
prevgrid = []
size = 70

for i in range(size):
    grid.append([0 for j in range(size)])
    prevgrid.append([0 for j in range(size)])


def evalLife(neighbors,row,cell):
    if prevgrid[row][cell] == 1:
        if 1 < neighbors < 4:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0

def checkNeighbors(col,cell):
    neighbors = 0
#---bottom neigh
    if cell < size-1:
        if prevgrid[col][cell+1] == 1:
            neighbors += 1
#---bottom right neigh
    if cell < size - 1 and col < size - 1:
        if prevgrid[col+1][cell+1] == 1:
            neighbors += 1
#---right neigh
    if col < size-1:
        if prevgrid[col+1][cell] == 1:
            neighbors += 1
#---top right neigh
    if col < size - 1 and cell > 0:
        if prevgrid[col+1][cell-1] == 1:
            neighbors += 1
#---top neigh
    if cell > 0:
        if prevgrid[col][cell-1] == 1:
            neighbors += 1
#---top left neigh
    if cell > 0 and col > 0:
        if prevgrid[col-1][cell-1] == 1:
            neighbors += 1
#---left neigh
    if col > 0:
        if prevgrid[col-1][cell] == 1:
            neighbors += 1
#---bottom left neigh
    if col > 0 and cell < size-1:
        if prevgrid[col-1][cell+1] == 1:
            neighbors += 1

    return neighbors




grid[10][10] = 1
grid[10][9] = 1
grid[9][8] = 1
grid[9][10] = 1
grid[8][10] = 1



def gameloop():
    for i in range(size):
        for j in range(size):
            prevgrid[i][j] = grid[i][j]
    for row in range(size):
        for cell in range(size):
            if grid[row][cell] == 1:
                pygame.draw.rect(window,pygame.Color(0,255,0),(row*10,cell*10,10,10))
            else:
                pygame.draw.rect(window,pygame.Color(255,255,255),(row*10,cell*10,10,10))
    pygame.display.update()
    fpsClock.tick(25)
    for row in range(size):
        for cell in range(size):
            grid[row][cell] = evalLife(checkNeighbors(row,cell),row,cell)
    gameloop()

gameloop()

