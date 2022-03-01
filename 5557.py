n = int(input())
dp = [[0]*21 for _ in range(n)]
board = list(map(int,input().split()))
dp[0][board[0]]=1
for i in range(1,n-1):
    for d in range(21):
        if dp[i-1][d]!=0:
            for next in [d+board[i],d-board[i]]:
                if 0<=next<=20:
                    dp[i][next]+=dp[i-1][d]
print(dp[n-2][board[n-1]])