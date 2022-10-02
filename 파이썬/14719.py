from collections import deque
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
board = [[0]*Y for _ in range(X)]
visited = [[0]*Y for _ in range(X)]
for y,tmp_H in enumerate(list(map(int, input().split()))):
    for x in range(tmp_H):
        board[x][y] = 1

def bfs(x,y):
    deq = deque()
    visited[x][y]=1
    deq.append((x,y))
    left, right, cnt = 0,0,0
    while deq:
        cur_x, cur_y = deq.popleft()
        visited[cur_x][cur_y]=1
        cnt+=1
        if left==0:
            next_x, next_y = cur_x,cur_y-1
            if 0<=next_y<Y and visited[next_x][next_y]==0:
                if board[next_x][next_y]==1:
                    left=1
                else:
                    deq.append((next_x, next_y))
        if right==0:
            next_x, next_y = cur_x,cur_y+1
            if 0<=next_y<Y and visited[next_x][next_y]==0:
                if board[next_x][next_y]==1:
                    right=1
                else:
                    deq.append((next_x, next_y))
    if left==1 and right==1:
        return cnt
    return 0

ans=0
for x in range(X):
    for y in range(Y):
        if visited[x][y]==0 and board[x][y]==0:
            ans += bfs(x,y)
print(ans)


