import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
m,n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int,input().split())))
visit = [[0]*n for _ in range(m)]

move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
words_num = 0

def dfs(x,y,c):
    if visit[x][y]==1:
        return
    else: visit[x][y]=1
    
    for tx, ty in move:
        if not(0<=x+tx<m and 0<=y+ty<n) or visit[x+tx][y+ty]==1:
            continue
        if board[x+tx][y+ty]==1:
            dfs(x+tx,y+ty,0)

    if c==1:
        global words_num
        words_num+=1

for i in range(m):
    for d in range(n):
        if board[i][d]==1:
            dfs(i,d,1)
print(words_num)