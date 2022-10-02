from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = []
visit = list( [0]*n for _ in range(n) )
deq = deque()
for _ in range(n):
    board.append(list(input()[:n]))
move = [(1,0),(-1,0),(0,1),(0,-1)]
result = []

def bfs(x,y):
    if visit[x][y]==1:
        return
    global n
    cnt=0
    visit[x][y]=1
    deq.append((x,y))
    while deq:
        x,y = deq.pop()
        visit[x][y]=1
        cnt += 1

        for dx,dy in move:
            if not ((0 <= x+dx <= n-1) and (0 <= y+dy <= n-1)):
                continue
            elif visit[x+dx][y+dy]==0 and board[x+dx][y+dy]=='1':
                deq.append((x+dx,y+dy))
                visit[x+dx][y+dy]=1
    result.append(cnt) 

for x in range(n):
    for y in range(n):
        if board[x][y]=='1':
            bfs(x,y)
result.sort()
print(len(result))
for _ in range(len(result)):
    print(result[_])