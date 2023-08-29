import sys
from collections import deque
input = sys.stdin.readline

# 준비물 초기화
N, M = map(int, input().split())
board = [ input().strip() for _ in range(N)]
rX, rY, bX, bY, gX, gY = 0, 0, 0, 0, 0, 0

for i in range(N):
    for d in range(M):
        if board[i][d] == "R":
            rX, rY = i,d
        elif board[i][d] == "B":
             bX, bY = i,d
        elif board[i][d] == "O":
            gX, gY = i,d

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rX][rY][bX][bY] = True
deq = deque()
deq.append([rX, rY, bX, bY, 0])


def moveBall(curX, curY, iX, iY):
    dist = 0
    nextX, nextY = curX, curY
    while board[nextX+iX][nextY+iY] != "#" and board[nextX][nextY] != "O":
        nextX += iX
        nextY += iY
        dist += 1
    return nextX, nextY, dist

def bfs():
    
    while deq:
        trX, trY, tbX, tbY, count = deq.popleft()
        if count >= 10:
            break
        
        for ix, iy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nrX, nrY, redDist = moveBall(trX, trY, ix, iy)
            nbX, nbY, blueDist = moveBall(tbX, tbY, ix, iy)
            if board[nbX][nbY] == "O": # 파란색 공이 빠지면 패스
                continue
            if board[nrX][nrY] == "O": # 빨간 공이 빠지면 성공
                return 1
            if nrX == nbX and nrY == nbY:
                if redDist > blueDist:
                    nrX += -ix
                    nrY += -iy
                elif redDist < blueDist:
                    nbX += -ix
                    nbY += -iy
            visited[nrX][nrY][nbX][nbY] = True
            deq.append([nrX, nrY, nbX, nbY, count+1])

    return 0

print(bfs())