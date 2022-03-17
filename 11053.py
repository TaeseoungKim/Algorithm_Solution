import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for d in range(i+1,n):
        if board[i]<board[d]:
            dp[d] = max(dp[d],dp[i]+1)

print(max(dp))
