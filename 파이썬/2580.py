import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]

blank = []

for i in range(9):
    for d in range(9):
        if board[i][d] == 0:
            blank.append([i,d])

def checkRow(x,num):
    for i in range(9):
        if board[x][i] == num:
            return False
    else:
        return True
    
def checkColumn(y,num):
    for i in range(9):
        if board[i][y] == num:
            return False
    else:
        return True

def checkSquare(x,y,num):
    cX = (x // 3) * 3
    cY = (y // 3) * 3
    for i in range(3):
        for d in range(3):
            if board[cX+i][cY+d] == num:
                return False
    return True


def backTracking(idx):
    if idx==len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)

    
    x = blank[idx][0]
    y = blank[idx][1]   

    for num in range(1,10):
        if checkRow(x,num) and checkColumn(y,num) and checkSquare(x,y,num):
            board[x][y] = num
            backTracking(idx+1)
            board[x][y] = 0

backTracking(0)