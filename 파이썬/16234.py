import sys
from collections import deque

input = sys.stdin.readline
N, MIN, MAX = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def bfs(pos):
    global isMoved
    deq = deque()
    deq.append(pos)
    unionArea = [pos]
    sumArea = board[pos[0]][pos[1]]
    visited[pos[0]][pos[1]] = True
    while deq:
        px,py = deq.popleft()
        for nx,ny in [(px+1,py),(px,py+1),(px-1,py),(px,py-1)]:
            if 0 <= nx < N and 0 <= ny < N and MIN <= abs(board[nx][ny]-board[px][py]) <= MAX and not visited[nx][ny]: 
                deq.append((nx,ny))
                unionArea.append((nx,ny))
                sumArea += board[nx][ny]
                visited[nx][ny] = True
                isMoved = True
    
    if not unionArea:
        return
    

    population = sumArea//len(unionArea)
    for x,y in unionArea:
        board[x][y] = population

day = 0
isMoved = False

while True: 

    visited = [[False for _ in range(N)] for _ in range(N)] 
    isMoved = False
    for i in range(N):
        for d in range(N):
            if not visited[i][d]:
                bfs((i,d))
    
    if not isMoved:
        break
    day += 1

print(day)


