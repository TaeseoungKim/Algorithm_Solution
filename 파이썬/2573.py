import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

def bfs(pos):
    x,y = pos
    visited[x][y] = True
    deq = deque()
    deq.append((x,y))
    meltArr = []

    while deq:
        meltCnt = 0
        px, py = deq.popleft()

        for nX, nY in [(px+1,py),(px,py+1),(px-1,py),(px,py-1)]:
            if not (0 <= nX < N and 0 <= nY < M):
                continue

            if board[nX][nY] > 0 and not visited[nX][nY]:
                deq.append((nX,nY))
                visited[nX][nY]=True
            
            if board[nX][nY] <= 0:
                meltCnt += 1
        
        meltArr.append((px,py,meltCnt))
    return meltArr
                
    
years = 0
visited = [[False for _ in range(M)] for _ in range(N)]
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    bfsCnt = 0
    
    
    for i in range(N):
        for d in range(M):
            if board[i][d] > 0 and not visited[i][d]:
                meltArr = bfs((i,d))
                bfsCnt += 1

    for x,y,meltCnt in meltArr:
        if board[x][y] - meltCnt <= 0:
            board[x][y] = 0
        else: board[x][y] -= meltCnt


    if bfsCnt != 1:
        break

    years += 1

if bfsCnt == 0:
    print(0)
else:
    print(years)