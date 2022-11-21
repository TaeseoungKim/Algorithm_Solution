from collections import deque
N = 5

board = [[0 for d in range(N)] for i in range(N)]
for i in range(N):
    print(board[i])


def bfs(pos):
    queue = deque()
    queue.append(pos)
    x, y = pos
    visited = [[False for d in range(N)] for i in range(N)]
    visited[x][y] = True

    while queue:
        px, py = queue.popleft()
        if px == N-1 and py == N-1:
            return True

        for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty]:
                visited[tx][ty] = True
                queue.append((tx, ty))


bfs((0, 0))
