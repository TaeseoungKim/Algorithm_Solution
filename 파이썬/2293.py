import sys
input = sys.stdin.readline
n,k = map(int, input().split())
board = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0]=1

for coin in board:
    for won in range(1,k+1):
        if won-coin>=0:
            dp[won] += dp[won-coin]

print(dp[k])

