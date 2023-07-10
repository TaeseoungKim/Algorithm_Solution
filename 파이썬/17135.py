from itertools import combinations
import sys
from copy import deepcopy
input = sys.stdin.readline
N, M, D = map(int, input().split())
inputBoard = []
for i in range(N):
    inputBoard.append(list(map(int, input().split())))


def moveMonster(board):
    for i in range(N-1, -1, -1):
        if i == 0:
            board[i] = [0 for _ in range(M)]
        else:
            board[i] = deepcopy(board[i-1])


def calDistant(source, destination):
    sx, sy = source
    dx, dy = destination
    return abs(dx-sx) + abs(dy-sy)


maxKill = 0
for archer in list(combinations([x for x in range(M)], 3)):
    board = deepcopy(inputBoard)

    tempKill = 0
    for _ in range(N):
        ableKill = [[], [], []]
        for i in range(N):
            for d in range(M):
                if board[i][d] == 1:
                    for x in range(len(archer)):
                        dist = calDistant((N, archer[x]), (i, d))
                        if D >= dist:
                            ableKill[x].append((i, d, dist))
        for i in range(len(archer)):
            ableKill[i] = sorted(ableKill[i], key=lambda x: (x[2], x[1]))

        killedSet = set()

        for i in range(3):
            if len(ableKill[i]) != 0:
                x, y, _ = ableKill[i][0]
                board[x][y] = "Killed"
                killedSet.add((ableKill[i][0][0], ableKill[i][0][1]))

        tempKill += len(killedSet)
        moveMonster(board)

    maxKill = max(maxKill, tempKill)
print(maxKill)
