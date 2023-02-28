import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def left_Monitor(i, d, board):
    for t in range(d-1, -1, -1):
        if board[i][t] == 6:
            break
        if board[i][t] == 0:
            board[i][t] = '#'


def right_Monitor(i, d, board):
    global M
    for t in range(d+1, M):
        if board[i][t] == 6:
            break
        if board[i][t] == 0:
            board[i][t] = '#'


def top_Monitor(i, d, board):
    for t in range(i-1, -1, -1):
        if board[t][d] == 6:
            break
        if board[t][d] == 0:
            board[t][d] = '#'


def bottom_Monitor(i, d, board):
    global N
    for t in range(i+1, N):
        if board[t][d] == 6:
            break
        if board[t][d] == 0:
            board[t][d] = '#'


def calculateBlank(board):
    global N, M, answer

    sumNum = 0
    for i in range(N):
        for d in range(M):
            if board[i][d] == 0:
                sumNum += 1

    answer = min(answer, sumNum)


def solve(cctvCnt, board):
    if cctvCnt == len(cctv):
        calculateBlank(board)
        return

    x, y = cctv[cctvCnt]
    if board[x][y] == 1:
        tempBoard = deepcopy(board)
        left_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        right_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        top_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        bottom_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)
    elif board[x][y] == 2:
        tempBoard = deepcopy(board)
        top_Monitor(x, y, tempBoard)
        bottom_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        left_Monitor(x, y, tempBoard)
        right_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

    elif board[x][y] == 3:
        tempBoard = deepcopy(board)
        top_Monitor(x, y, tempBoard)
        left_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        left_Monitor(x, y, tempBoard)
        bottom_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        bottom_Monitor(x, y, tempBoard)
        right_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        right_Monitor(x, y, tempBoard)
        top_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

    elif board[x][y] == 4:
        tempBoard = deepcopy(board)
        right_Monitor(x, y, tempBoard)
        top_Monitor(x, y, tempBoard)
        left_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        top_Monitor(x, y, tempBoard)
        left_Monitor(x, y, tempBoard)
        bottom_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        left_Monitor(x, y, tempBoard)
        bottom_Monitor(x, y, tempBoard)
        right_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

        tempBoard = deepcopy(board)
        bottom_Monitor(x, y, tempBoard)
        right_Monitor(x, y, tempBoard)
        top_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)

    elif board[x][y] == 5:
        tempBoard = deepcopy(board)
        top_Monitor(x, y, tempBoard)
        left_Monitor(x, y, tempBoard)
        bottom_Monitor(x, y, tempBoard)
        right_Monitor(x, y, tempBoard)
        solve(cctvCnt+1, tempBoard)
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

cctv = list()
for i in range(N):
    for d in range(M):
        if 1 <= board[i][d] <= 5:
            cctv.append((i, d))

cctvNumber = len(cctv)
cctvCnt = 0
answer = sys.maxsize
solve(cctvCnt, board)
print(answer)
