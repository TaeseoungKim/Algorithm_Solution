from itertools import combinations, product
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
visited = [[False for d in range(M)] for i in range(N)]
virus = []
for i in range(N):
    for d in range(M):
        if board[i][d] == 2:
            virus.append((i, d))
prodResult = list(product(list(range(N)), list(range(M))))
allComb = list(combinations(prodResult, 3))


def bfs(pos, board, visited):
    queue = deque()
    queue.append(pos)
    visited[pos[0]][pos[1]] = True
    while queue:
        px, py = queue.popleft()

        for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
            if 0 <= tx < N and 0 <= ty < M and board[tx][ty] == 1:
                continue

            if 0 <= tx < N and 0 <= ty < M and visited[tx][ty] == False:
                visited[tx][ty] = True
                board[tx][ty] = 2
                queue.append((tx, ty))


maxSafe = 0
for wall_1, wall_2, wall_3 in allComb:
    x1, y1 = wall_1
    x2, y2 = wall_2
    x3, y3 = wall_3
    if (board[x1][y1] == 0 and board[x2][y2] == 0 and board[x3][y3] == 0):
        newBoard = deepcopy(board)
        newVisited = deepcopy(visited)
        newBoard[x1][y1] = 1
        newBoard[x2][y2] = 1
        newBoard[x3][y3] = 1
        newMax = 0
        for vx, vy in virus:
            if newVisited[vx][vy] == False:
                bfs((vx, vy), newBoard, newVisited)
        for i in range(N):
            for d in range(M):
                if newBoard[i][d] == 0:
                    newMax += 1
        maxSafe = max(maxSafe, newMax)
print(maxSafe)
