#스도쿠의 원리: 행, 열, 3x3에 같은 숫자가 있지만 않으면 된다.
import sys
input = sys.stdin.readline
def colCheck(x,num):
    for d in range(9):
        if board[x][d]==num:
            return False
    return True

def rowCheck(y,num):
    for d in range(9):
        if board[d][y]==num:
            return False
    return True

def squareCheck(x,y,num):
    x = (x//3)*3
    y = (y//3)*3
    for tx in range(x,x+3):
        for ty in range(y,y+3):
            if board[tx][ty]==num:
                return False
    return True


def dfs(depth):
    if depth==Maxdepth:
        for i in range(9):
            print(board[i])
        exit()
    x,y = zeros[depth]
    for num in range(1,10):
        if colCheck(x,num) and rowCheck(y,num) and squareCheck(x,y,num):
            board[x][y]=num
            dfs(depth+1)
            board[x][y]=0

board = list(list(map(int, input().strip())) for _ in range(9))
zeros = []
for i in range(9):
    for d in range(9):
        if board[i][d]==0:
            zeros.append((i,d))
Maxdepth = len(zeros)
dfs(0)