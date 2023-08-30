

import sys
from copy import deepcopy
input = sys.stdin.readline

dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

board = []
fishInfo = dict()
for i in range(4):
    tempArr = list(map(int, input().strip().split(" ")))
    a1,b1, a2,b2, a3,b3, a4,b4 = tempArr
    fishInfo[a1] = [i,0,b1-1] # x, y, direction
    fishInfo[a2] = [i,1,b2-1]
    fishInfo[a3] = [i,2,b3-1]
    fishInfo[a4] = [i,3,b4-1]
    board.append([[a1,b1-1], [a2,b2-1], [a3,b3-1], [a4,b4-1]]) 


def fishMove(board, fishInfo, sharkPos):
    sx, sy = sharkPos
    for i in range(1,17):
        if fishInfo[i]!=False:
            x, y, d = fishInfo[i]
            dx, dy = dir[d]
            nextX, nextY = x+dx, y+dy
            count = 0

            while count < 8:
                if  0 <= nextX < 4 and 0 <= nextY < 4:
                    if (nextX == sx and nextY == sy):
                        pass
                    elif board[nextX][nextY] == False: # 빈칸
                        fishInfo[board[x][y][0]] = [nextX, nextY, d]
                        board[nextX][nextY], board[x][y] = board[x][y], False
                        break
                    elif board[nextX][nextY] != False:
                        fishInfo[board[nextX][nextY][0]] = [x, y, board[nextX][nextY][1]]
                        fishInfo[board[x][y][0]] = [nextX, nextY, d]
                        board[x][y], board[nextX][nextY] = board[nextX][nextY], [board[x][y][0],d]
                        break

                if d == 7:
                    d = 0
                else: 
                    d += 1
                
                dx, dy = dir[d]
                nextX, nextY = x+dx, y+dy
                count += 1

maxValue = 0

def backTracking(prevBoard,sharkPos,prevSum,prevFishInfo):
    global maxValue
    board = deepcopy(prevBoard)
    fishInfo= deepcopy(prevFishInfo)
    sx, sy = sharkPos
    fishNum, fishDir =  board[sx][sy][0], board[sx][sy][1]
    sumValue = prevSum + fishNum
    maxValue = max(maxValue, sumValue)
    sharkDir = fishDir
    board[sx][sy] = False # 빈공간
    fishInfo[fishNum] = False

    fishMove(board, fishInfo, sharkPos)

    nextX, nextY = sx+dir[sharkDir][0], sy+dir[sharkDir][1]
    while 0 <= nextX < 4 and 0 <= nextY < 4 :
        if board[nextX][nextY] != False:
            backTracking(board, (nextX,nextY), sumValue, fishInfo)
        nextX, nextY = nextX+dir[sharkDir][0], nextY+dir[sharkDir][1]

backTracking(board, (0,0), 0, fishInfo)
print(maxValue)