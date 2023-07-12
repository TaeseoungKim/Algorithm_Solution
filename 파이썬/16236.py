import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

def bfs():
    distBoard = [[-1 for _ in range(N)] for _ in range(N)]
    sx, sy = sharkPos
    distBoard[sx][sy] = 0
    deq = deque()
    deq.append((sx,sy))

    while deq:
        px, py = deq.popleft()
        for nx, ny in [(px+1, py),(px, py+1),(px-1, py),(px, py-1)]:
            if (0 <= nx < N) and (0 <= ny < N)  and board[nx][ny] <= sharkSize:
                if distBoard[nx][ny] == -1 or distBoard[nx][ny] > distBoard[px][py]+1:
                    deq.append((nx,ny))
                    distBoard[nx][ny] = distBoard[px][py]+1 

    return distBoard

sharkPos = (0,0)
sharkSize = 2
resultTime = 0
curFeed = 0

while True:
    for i in range(N):
        for d in range(N):
            if board[i][d] == 9:
                sharkPos = (i,d)

    distBoard = bfs()
    ableBite = []
    minV = 9999

    for i in range(N):
        for d in range(N):
            if board[i][d]!=0 and board[i][d] < sharkSize:
                if distBoard[i][d] == -1:
                    continue
                if minV > distBoard[i][d]:
                    ableBite = [(i, d)]
                    minV = distBoard[i][d]
                elif minV == distBoard[i][d]:
                    ableBite.append((i,d))
    
    if ableBite:
        ableBite.sort(key= lambda x: (x[0],x[1]))
        x,y = ableBite[0]
        resultTime += distBoard[x][y]
        curFeed += 1
        board[x][y] = 9
        board[sharkPos[0]][sharkPos[1]] = 0

        if curFeed == sharkSize:
            sharkSize += 1
            curFeed = 0
    else:
        break
print(resultTime)


