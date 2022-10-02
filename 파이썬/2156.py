import sys
input = sys.stdin.readline
n = int(input())

board = list(int(input()) for _ in range(n))
dp = [[0]*2 for _ in range(n)] # [불연속, 연속]
dp[0][0],dp[0][1] = board[0],board[0]
max_V = board[0]
if n>=2:
    dp[1][0],dp[1][1] = board[1], dp[0][0]+board[1]
    max_V = dp[0][0]+board[1]
    for i in range(2,n):
        dp[i][0] = max(dp[i-2][0],dp[i-2][1])+board[i] # 불연속
        dp[i][1] = max(dp[i-1][0]+board[i],dp[i-1][1])
        max_V = max(max_V,dp[i][0],dp[i][1])
print(max_V)