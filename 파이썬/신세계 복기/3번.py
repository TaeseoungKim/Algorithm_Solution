from itertools import combinations
from copy import deepcopy


def wallCheck(board, n):
    Check = True
    for i in range(n-1):
        for d in range(n-1):
            if board[i][d] == False and board[i+1][d] == False and board[i][d+1] == False and board[i+1][d+1] == False:
                Check = False
    return Check


def solution(n, walls):
    board = [[False for d in range(n)] for i in range(n)]
    wallCnt = 0
    noWall = []

    for x, y in walls:
        board[x][y] = True
        wallCnt += 1
    wallCnt = (n*n)-wallCnt

    for i in range(n):
        for d in range(n):
            if board[i][d] == False:
                noWall.append((i, d))
    if wallCheck(board, n):
        return 0

    Answer = False
    for addWallCnt in range(1, wallCnt+1):

        for temp in list(combinations(noWall, addWallCnt)):
            newBoard = deepcopy(board)
            for tx, ty in temp:

                newBoard[tx][ty] = True
            if wallCheck(newBoard, n) == True:
                return addWallCnt
                Answer = addWallCnt
                break
        if Answer != False:
            break

    return Answer
