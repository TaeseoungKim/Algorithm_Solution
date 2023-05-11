import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    curValue = 1
    while queue:
        px, py = queue.popleft()
        for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
            if (0 <= tx < N) and (0 <= ty < M) and board[tx][ty] == 1 and visited[tx][ty] == False:
                visited[tx][ty] = True
                queue.append((tx, ty))
                curValue += 1
    return curValue


N, M, K = map(int, input().split(" "))
board = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
maxValue = -1

for i in range(K):
    r, c = map(int, input().split(" "))
    board[r-1][c-1] = 1


for i in range(N):
    for d in range(M):
        if board[i][d] == 1 and visited[i][d] == False:
            nextValue = bfs(i, d)
            maxValue = max(maxValue, nextValue)
print(maxValue)
