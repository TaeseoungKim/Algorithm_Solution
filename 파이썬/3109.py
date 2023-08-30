R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

def dfs(pos):
    curX, curY = pos

    if curY==C-1:
        return True

    for nextX, nextY in [(curX-1,curY+1),(curX,curY+1),(curX+1,curY+1)]:
        if 0 <= nextX < R and 0 <= nextY < C and board[nextX][nextY]!="x" and visited[nextX][nextY]!=True:
            visited[nextX][nextY] = True
            return dfs((nextX, nextY))
    return False

answer = 0
for i in range(R):
    if dfs((i,0)):
        answer += 1

print(answer)

