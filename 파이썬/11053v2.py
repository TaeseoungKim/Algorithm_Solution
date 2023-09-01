import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1,N):
    maxPrev = board[i-1]
    for d in range(i):
        if board[i] > board[d]:
            dp[i] = max(dp[i], dp[d]+1)

print(max(dp))