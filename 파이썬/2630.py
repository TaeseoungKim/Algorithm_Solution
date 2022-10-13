from copy import copy, deepcopy
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split(" "))) for i in range(N)]
white = 0
blue = 0


def allSameCheck(board, length):
    initV = board[0][0]
    for i in range(length):
        for d in range(length):
            if board[i][d] != initV:
                return False
    return True


def sol(board, length):
    global white, blue
    mid = length//2

    if allSameCheck(board, length):
        if board[0][0] == 0:
            white += 1
        else:
            blue += 1
    else:
        sol(deepcopy([tempBoard[:mid]
            for tempBoard in board[:mid]]), mid)  # 4사분면
        sol(deepcopy([tempBoard[:mid]
            for tempBoard in board[mid:]]), mid)  # 3사분면
        sol(deepcopy([tempBoard[mid:]
            for tempBoard in board[:mid]]), mid)  # 1사분면
        sol(deepcopy([tempBoard[mid:]
            for tempBoard in board[mid:]]), mid)  # 2사분면


sol(board, N)

print(white)
print(blue)
