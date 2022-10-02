import sys,heapq
from collections import deque

#dfs로만 해결될 것 같은 문제는
#bfs와 heap을 이용해서 해결할 수 있다
input = sys.stdin.readline

m, n = map(int, input().split())
board = []
visit = [[0]*n for _ in range(m)]

for _ in range(m):
    board.append(list(map(int,input().split()[:n])))

#상하좌우
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(tx,ty):
    prior = [] 
    visit[tx][ty]=1
    heapq.heappush(prior,(-board[tx][ty],tx,ty))

    while prior:
        _,x,y = heapq.heappop(prior)
        
        for px, py in move:
            if not(0<=x+px<m) or not(0<=y+py<n):
                continue
            if board[x][y]>board[x+px][y+py]:
                if visit[x+px][y+py] == 0:
                    heapq.heappush(prior,(-board[x+px][y+py],x+px,y+py))
                visit[x+px][y+py]+=visit[x][y]
    return

bfs(0,0)
print(visit[m-1][n-1])
