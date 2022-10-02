from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(k):
        x,y = map(int, input().split())
        board[y][x]=1

    def dfs(x,y):
        global result
        result += 1
        deq = deque()
        deq.append((x,y))
        while deq:
            px,py = deq.pop()
            visited[px][py]=1
            for tx,ty in move:
                if (0<= tx+px <n and 0<= ty+py <m) and board[tx+px][ty+py]==1 and visited[tx+px][ty+py]==0 :
                    deq.append((tx+px,ty+py))

    result = 0
    for x in range(n):
        for y in range(m):
            if board[x][y]==1 and visited[x][y]==0:
                dfs(x,y)
    print(result)