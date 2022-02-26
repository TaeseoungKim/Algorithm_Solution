from collections import deque
def bfs(x,y,color):
    visited[x][y]=1
    deq = deque()
    deq.append((x,y))
    cnt = 1
    while deq:
        cur_x, cur_y = deq.popleft()
        for tmp_x, tmp_y in move:
            next_x = cur_x+tmp_x
            next_y = cur_y+tmp_y
            if 0<=next_x<m and 0<=next_y<n and color==board[next_x][next_y] and visited[next_x][next_y]==0:
                visited[next_x][next_y]=1
                deq.append((next_x,next_y))
                cnt+=1
    return cnt

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(m)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0]*n for _ in range(m)]
white = 0
blue = 0

for x in range(m):
    for y in range(n):
        if visited[x][y]==0:
            if board[x][y]=="W":
                white += bfs(x,y,board[x][y])**2
            else: blue += bfs(x,y,board[x][y])**2

print(white,blue)