from collections import deque

def bfs(x,y,board,visit,move):
    deq = deque()
    deq.append((x,y,0))
    visit[x][y][0]=1
    while deq:
        cur_x,cur_y,crashed = deq.popleft()
        if cur_x==n-1 and cur_y==m-1:
            return visit[cur_x][cur_y][crashed]
        for dx, dy in move:
            next_x = cur_x+dx
            next_y = cur_y+dy
            if 0<=next_x<n and 0<=next_y<m:
                if board[next_x][next_y]==0 and visit[next_x][next_y][crashed]==0:
                    visit[next_x][next_y][crashed]=visit[cur_x][cur_y][crashed]+1
                    deq.append((next_x,next_y,crashed))

                elif board[next_x][next_y]==1 and crashed==0 and visit[next_x][next_y][crashed+1]==0:
                    visit[next_x][next_y][crashed+1]=visit[cur_x][cur_y][crashed]+1
                    deq.append((next_x,next_y,crashed+1))
    return -1
n, m = map(int,input().split())
board = [list(map(int, input())) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
print(bfs(0,0,board,visit,move))