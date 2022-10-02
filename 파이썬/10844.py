import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*11 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1]
    for d in range(1,10):
        dp[i][d] = dp[i-1][d-1]+dp[i-1][d+1]

print(sum(dp[n])%1000000000)