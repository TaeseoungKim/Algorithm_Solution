n=int(input())
dp = [0,1,2,3,7]
if n<5:
    print(dp[n])
else:
    for i in range(5,n+1):
        dp.append(dp[i-1]+dp[i-2]*2)
    print(dp[n])