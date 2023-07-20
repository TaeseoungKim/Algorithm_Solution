import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

def bfs(pos):
    deq = deque()
    deq.append(pos)

    while deq:
        x,y = deq.popleft()
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]!=-1:
                    continue
                
                if board[nx][ny] == '0': # 방
                        visited[nx][ny] = visited[x][y]
                        deq.appendleft((nx,ny))

                elif board[nx][ny] == '1': # 벽
                        visited[nx][ny] = visited[x][y]+1
                        deq.append((nx,ny))

visited[0][0]=0
bfs((0,0))
print(visited[N-1][M-1])