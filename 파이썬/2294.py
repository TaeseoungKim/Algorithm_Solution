import sys
input = sys.stdin.readline
n,k = map(int, input().split())
board = [int(input()) for _ in range(n)]
dp = [-1]*(k+1)
dp[0] = 0


for won in range(k):
    if dp[won]==-1 :
        continue
    for coin in board:
        if won+coin>k:
            continue
        if dp[won+coin]==-1 or dp[won+coin] > dp[won]+1:
            dp[won+coin] = dp[won]+1
print(dp[k])