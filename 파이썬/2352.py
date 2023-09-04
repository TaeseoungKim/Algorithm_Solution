import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
for i in range(N):
    board[i] -= 1

dp = [board[0]]

for i in range(N):
    if board[i] > dp[-1]:
        dp.append(board[i])
    else:
        idx = bisect_left(dp, board[i])
        dp[idx] = board[i]

print(len(dp))