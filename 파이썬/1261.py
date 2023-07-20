import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
pathBoard = [[(0,0) for _ in range(M)] for _ in range(N)]

MinBreakedWall = 10000





def dfs(pos,breakedWall):
    global MinBreakedWall
    x,y = pos
    dist, BW = pathBoard[x][y]

    if x==N-1 and y==M-1:
        MinBreakedWall = min(MinBreakedWall,breakedWall)
        return

    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
              continue
        
        if board[nx][ny] == '0': # 방
            visited[nx][ny]=True
            
            dfs((nx,ny),breakedWall)
            visited[nx][ny]=False
            
        elif board[nx][ny] == '1': # 벽
             if MinBreakedWall > breakedWall+1:
                visited[nx][ny]=True
                board[nx][ny] = '0'
                dfs((nx,ny),breakedWall+1)
                visited[nx][ny]=False
                board[nx][ny] = '1'


visited[0][0]=True
dfs((0,0),0)
print(MinBreakedWall)