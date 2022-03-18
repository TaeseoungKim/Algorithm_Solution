from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
board = list( list(map(int, input().split())) for _ in range(n))

dp = [[0]*m for _ in range(n)] # 밑, 왼, 우
visited = [[[0,0,0] for _ in range(m) ] for _ in range(n)]
temp = [[0,0] for _ in range(m)]

def solution(row):
    #왼쪽에서 오른쪽으로 갈 경우를 임시로 저장한다
    for i in range(m):
        if i==0:
            temp[i][0] = dp[row-1][i]+board[row][i]
            continue
        temp[i][0] = max(dp[row-1][i],temp[i-1][0])+board[row][i]
    #오른쪽에서 왼쪽으로 갈 경우를 임시로 저장한다
    for i in range(m-1,-1,-1):
        if i==m-1:
            temp[i][1] = dp[row-1][i]+board[row][i]
            continue
        temp[i][1] = max(dp[row-1][i],temp[i+1][1])+board[row][i]

    #위에서 왼,우의 임시 값들을 이용하여 최종 dp를 완성한다
    for i in range(m):
        if i==0: 
            dp[row][i] = max(dp[row-1][i],temp[i+1][1])+board[row][i]
            continue
        if i==m-1: 
            dp[row][i] = max(dp[row-1][i],temp[i-1][0])+board[row][i]
            continue
        dp[row][i] = max(dp[row-1][i],temp[i-1][0],temp[i+1][1])+board[row][i]
if n==1 and m==1:
    print(board[0][0])
elif m==1:
    dp[0][0]=board[0][0]
    for i in range(n):
        if i==0:
            dp[0][0]=board[0][0]
            continue
        dp[i][0]+=dp[i-1][0]+board[i][0]
        print(dp[n-1][m-1])
else:
    for i in range(m):
        if i==0:
            dp[0][0]=board[0][0]
            continue
        dp[0][i]+=dp[0][i-1]+board[0][i]

    if n!=1:
        for i in range(1,n):
            solution(i)
    print(dp[n-1][m-1])
