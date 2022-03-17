from collections import deque
import sys
input = sys.stdin.readline
move = [(1,0),(-1,0),(0,1),(0,-1)]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]
max_V = 0
def dfs(x,y):
    global max_V
    deq = deque()
    deq.append((x,y))
    while deq:
        tx, ty = deq.pop()
        for next_x, next_y in [(tx+1,ty),(tx-1,ty),(tx,ty+1),(tx,ty-1)]:
            if 0<=next_x<n and 0<=next_y<n and board[next_x][next_y] > board[tx][ty]:
                if dp[next_x][next_y] < dp[tx][ty]+1 :
                    dp[next_x][next_y] = dp[tx][ty]+1
                    max_V = max(max_V, dp[next_x][next_y])
                    deq.append((next_x,next_y))
                    

for i in range(n):
    for d in range(n):
        if dp[i][d]==1:
            bfs(i,d)
print(max_V)