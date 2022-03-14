import sys
input = sys.stdin.readline
n = int(input())
dp = [[],[0,1]] #1자리
for i in range(2,n+1):
    dp.append([dp[i-1][0]+dp[i-1][1],dp[i-1][0]])
print(dp[-1][0]+dp[-1][1])