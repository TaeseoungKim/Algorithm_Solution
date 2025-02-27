from collections import deque
N = 3

board = [[0 for d in range(N)] for i in range(N)]
for i in range(N):
    print(board[i])


def bfs(pos):
    visited = [[False for d in range(N)] for i in range(N)]
    x, y = pos
    visited[x][y] = True
    queue = deque()
    queue.append(pos)

    while queue:
        px, py = queue.popleft()
        for i in range(N):
            print(visited[i])
        print()
        print()

        for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty]:
                visited[tx][ty] = True
                queue.append((tx, ty))


bfs((0, 0))
# def dfs()
