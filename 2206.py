from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().strip())))
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
print("visitt",visit)
def dfs(v,c):
    x,y = v
    if x==n and y==m:
        return
    for tx, ty in move:
        print(x,y,tx,ty)
        if 0<=x+tx<n and 0<=y+ty<n:
            if c==0:
                if board[x+tx][y+ty]==0:
                    if visit[x+tx][y+ty][0]!=0:
                        visit[x+tx][y+ty][0]=min(visit[x][y][0]+1,visit[x+tx][y+ty][0])
                    else:
                        visit[x+tx][y+ty][0]=visit[x][y][0]+1
                    dfs((x+tx,y+ty),c)
            elif c==1 and board[x+tx][y+ty]==1:
                if visit[x+tx][y+ty][0]!=0:
                    visit[x+tx][y+ty][0]=min(visit[x][y][1]+1,visit[x+tx][y+ty][1])
                else:
                    visit[x+tx][y+ty][0]=visit[x][y][1]+1
                dfs((x+tx,y+ty),c-1)
            elif c==1 and board[x+tx][y+ty]==0:
                if visit[x+tx][y+ty][1]!=0:
                    visit[x+tx][y+ty][1]=min(visit[x][y][1]+1,visit[x+tx][y+ty][1])
                else:
                    visit[x+tx][y+ty][1]=visit[x][y][1]+1
                dfs((x+tx,y+ty),c)
                
            

dfs((0,0),1)
print(visit[n-1][m-1])
    