import sys
n = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))

dp = [ 1 for _ in range(n) ]

for i in range(n):
    for j in range(i):
        if list[i] < list[j]:
            dp[i] = max(dp[j] + 1 , dp[i])

print(max(dp))

