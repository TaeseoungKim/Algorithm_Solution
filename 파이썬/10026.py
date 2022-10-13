import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [input().strip() for i in range(N)]


def normalBFS(pos):
    queue = deque()
    queue.append(pos)
    normalVisited[pos[0]][pos[1]] = True

    while queue:
        px, py = queue.popleft()
        for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
            if 0 <= tx < N and 0 <= ty < N and not normalVisited[tx][ty] and (board[pos[0]][pos[1]] == board[tx][ty]):
                normalVisited[tx][ty] = True
                queue.append((tx, ty))


normalVisited = [[False for d in range(N)] for i in range(N)]
normalResult = 0
for i in range(N):
    for d in range(N):
        if not normalVisited[i][d]:
            normalBFS((i, d))
            normalResult += 1

print(normalResult)


def blindBFS(pos):
    queue = deque()
    queue.append(pos)
    blindVisited[pos[0]][pos[1]] = True

    if board[pos[0]][pos[1]] == 'B':
        while queue:
            px, py = queue.popleft()
            for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
                if 0 <= tx < N and 0 <= ty < N and not blindVisited[tx][ty] and (board[pos[0]][pos[1]] == board[tx][ty]):
                    blindVisited[tx][ty] = True
                    queue.append((tx, ty))
    else:
        while queue:
            px, py = queue.popleft()
            for tx, ty in [(px+1, py), (px, py+1), (px-1, py), (px, py-1)]:
                if 0 <= tx < N and 0 <= ty < N and not blindVisited[tx][ty] and (board[tx][ty] == 'R' or board[tx][ty] == 'G'):
                    blindVisited[tx][ty] = True
                    queue.append((tx, ty))


blindVisited = [[False for d in range(N)] for i in range(N)]
blindResult = 0
for i in range(N):
    for d in range(N):
        if not blindVisited[i][d]:
            blindBFS((i, d))
            blindResult += 1

print(blindResult)
