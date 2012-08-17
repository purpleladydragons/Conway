import os
import random
import time
import pygame


pygame.init()
fpsClock = pygame.time.Clock()
squaresize = 600

position = 300, 100
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])

window = pygame.display.set_mode((squaresize,squaresize))

grid = []
prevgrid = []
startgrid = []
size = squaresize/10

for i in range(size):
    grid.append([0 for j in range(size)])
    prevgrid.append([0 for j in range(size)])
    startgrid.append([0 for j in range(size)])


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



def generateGlider(col=10,cell=10): 
#need to check for legal glider position
    grid[col][cell] = 1
    grid[col][cell-1] = 1
    grid[col-1][cell-2] = 1
    grid[col-1][cell] = 1
    grid[col-2][cell] = 1

def generateRandom(n):
    for x in range(n):
        grid[random.randint(0,size-1)][random.randint(0,size-1)] = 1

def saveStart():
    for i in range(size):
        for j in range(size):
            startgrid[i][j] = grid[i][j]
    with open('conway.txt','a') as f:
        f.write('\n---------------New Conway-----------------\n')
        for col in startgrid:
            for cell in col:
                f.write(str(cell)+" ")
            f.write("\n")
        f.write('\n---------------End Conway-----------------\n')




def gameloop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
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
    time.sleep(.1)
    gameloop()

generateGlider(5,8)
generateRandom(300)
saveStart()
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
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
    time.sleep(.1)


