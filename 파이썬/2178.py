from collections import deque
def bfs(x,y):
    deq = deque()
    deq.append((x,y))

    while deq:
        cur_x, cur_y = deq.popleft()
        if cur_x==n-1 and cur_y==m-1:
            return visit[cur_x][cur_y]
        for tmp_x, tmp_y in move:
            next_x = cur_x+tmp_x
            next_y = cur_y+tmp_y
            if 0<=next_x<n and 0<=next_y<m and visit[next_x][next_y]==0 and board[next_x][next_y]==1:
                visit[next_x][next_y]=1+visit[cur_x][cur_y]
                deq.append((next_x,next_y))

n,m = map(int, input().split())
board = [list(map(int,input().strip()) )for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
visit = [[0]*m for _ in range(n)]
visit[0][0]=1
print(bfs(0,0))
