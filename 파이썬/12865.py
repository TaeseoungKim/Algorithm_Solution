n, k = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for d in range(1,k+1):
        weight = stuff[i-1][0]
        value = stuff[i-1][1]
        if weight>d:
            dp[i][d] = dp[i-1][d]
        else:
            dp[i][d] = max(dp[i-1][d], value+dp[i-1][d-weight])
print(dp[n][k])
    