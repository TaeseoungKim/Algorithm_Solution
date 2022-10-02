import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
op = list(map(int, input().split()))
max_V, min_V = -10**9,10**9
def dfs(idx,val):
    global max_V, min_V
    if sum(op)==0:
        max_V = max(max_V, val)
        min_V = min(min_V, val)
        return

    if op[0]!=0:
        op[0]-=1
        dfs(idx+1,val+board[idx+1])
        op[0]+=1

    if op[1]!=0:
        op[1]-=1
        dfs(idx+1,val-board[idx+1])
        op[1]+=1

    if op[2]!=0:
        op[2]-=1
        dfs(idx+1,val*board[idx+1])
        op[2]+=1

    if op[3]!=0:
        op[3]-=1
        if val<0:
            dfs(idx+1,-((-val)//board[idx+1]))
        else: dfs(idx+1,val//board[idx+1])
        op[3]+=1

dfs(0,board[0])
print(max_V)
print(min_V)