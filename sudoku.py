import numpy

grid = [[9,0,0,0,7,0,0,0,0],
        [2,0,0,0,9,0,0,5,3],
        [0,6,0,0,1,2,4,0,0],
        [8,4,0,0,0,1,0,9,0],
        [5,0,0,0,0,0,8,0,0],
        [0,3,1,0,0,4,0,0,0],
        [0,0,3,7,0,0,6,8,0],
        [0,9,0,0,5,0,7,4,1],
        [4,7,0,0,0,0,0,0,0]]

grid2 =[[9,1,4,3,7,5,2,6,8],
        [2,8,7,4,9,6,1,5,3],
        [3,6,5,8,1,2,4,7,9],
        [8,4,6,5,2,1,3,9,7],
        [5,2,9,6,3,7,8,1,4],
        [7,3,1,9,8,4,5,2,6],
        [1,5,3,7,4,9,6,8,2],
        [6,9,8,2,5,3,7,4,1],
        [4,7,2,1,6,8,9,3,5]]

grid1 =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
#print(numpy.matrix(grid1))

def possible(y,x,n):
    global grid1
    for i in range(0,9):
        if (grid1[y][i] == n):
            #print(grid1[y][i], end=", ")
            return False
    for i in range(0,9):
        if (grid1[i][x] == n):
            #print(grid[y][i], end=" ")
            return False
    x9 = (x//3) * 3
    y9 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if (grid1[y9 + i][x9 + j] == n):
                return False
    return True

def solve():
    for y in range(9):
        for x in range(9):
            if (grid1[y][x] == 0):
                for n in range(1,10):
                    if possible(y, x, n):
                        grid1[y][x] = n
                        solve()
                        grid1[y][x] = 0
                return
    print(numpy.matrix[grid1])

solve()
#print(possible(4,4,5))
# print(possible(1,0,1))
# print(possible(2,0,4))
# print(possible(3,0,4))
# print(possible(5,0,5))
# print(possible(6,0,2))