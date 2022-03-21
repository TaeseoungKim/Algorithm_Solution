import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n+1)]

for i in range(10):
    dp[1][i]=1
for i in range(2,n+1):
    for d in range(10):
        for k in range(d+1):
            dp[i][d] += dp[i-1][k]

print(sum(dp[n])%10007)
