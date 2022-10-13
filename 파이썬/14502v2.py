from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for i in range(N)]

blanks = []

for i in range(N):
    for d in range(M):
        if board[i][d] == 0:
            blanks.append((i, d))


# 벽을 딱 3개 세워야 하고,

for Walls in combinations(blanks, 3):
    print(i)
