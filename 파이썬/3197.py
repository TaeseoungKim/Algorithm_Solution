

import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = [input().rstrip() for i in range(R)]
for i in range(R):
    print(board[i])