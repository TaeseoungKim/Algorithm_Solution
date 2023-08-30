import sys
from collections import deque
input = sys.stdin.readline
count = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(N)]
    deq = deque()

    deq.append((0,0))
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[0][0] = board[0][0]

    while deq:
        curX, curY = deq.popleft()
        
        for nextX, nextY in [(curX+1, curY),(curX, curY+1),(curX-1, curY),(curX, curY-1)]:
            if 0 <= nextX < N and 0 <= nextY < N:
                if visited[nextX][nextY] == -1:
                    visited[nextX][nextY] = visited[curX][curY]+board[nextX][nextY]
                    deq.append((nextX,nextY))
                elif visited[nextX][nextY] != -1 and visited[nextX][nextY] > visited[curX][curY]+board[nextX][nextY]:
                    visited[nextX][nextY] = visited[curX][curY]+board[nextX][nextY]
                    deq.append((nextX,nextY))
    
    answer = "Problem "+str(count) +": "+str(visited[N-1][N-1]) 
    print(answer)
    count += 1