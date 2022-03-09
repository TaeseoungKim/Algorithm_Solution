n=int(input())
board = list()
for _ in range(n):
    board.append(tuple(map(int, input().split())))
MAX_VALUE = 2**31-1
visited = [0]*n

def dp(board,n):
    if n==1:
        return 0
    
    cal_cnt = MAX_VALUE
    for i in range(n-1):
        cal_cnt = min(cal_cnt,dp([*board[:i],[board[i][0],board[i+1][1]],*board[i+2:]],n-1)+board[i][0]*board[i][1]*board[i+1][1])

    return cal_cnt

print(dp(board,n))