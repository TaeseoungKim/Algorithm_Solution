#dfs는 스택으로 구현하는 습관을 들이자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(v,cnt,visit):
    visit[v]=1
    if cnt>=4:
        return True
    elif len(board[v])==0:
        return False

    for i in board[v]:
        if visit[i]==0:
            if dfs(i,cnt+1,visit)==True:
                return True
            visit[i]=0

    return False

result = 0
visit = [0]*n
for i in range(n):
    if dfs(i,0,visit)==True:
        result=1
        break
    visit[i]=0
print(result)
    