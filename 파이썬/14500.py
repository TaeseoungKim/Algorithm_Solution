import sys


def calExShape(x, y):

    shapeArr = [[(x, y-1), (x, y), (x, y+1), (x-1, y)], [(x, y-1), (x, y), (x, y+1), (x+1, y)],
                [(x-1, y), (x, y), (x+1, y), (x, y+1)], [(x-1, y), (x, y), (x+1, y), (x, y-1)]]

    sumValue = 0
    for shape in shapeArr:
        tempSum = 0
        for tx, ty in shape:
            if 0 <= tx < N and 0 <= ty < M:
                tempSum += board[tx][ty]
            else:
                tempSum = 0
                break
        sumValue = max(sumValue, tempSum)

    return sumValue


def dfs(x, y, visited, cnt, curNum):
    global MaxNum
    visited[x][y] = board[x][y]
    curNum = curNum+board[x][y]

    if cnt == 4:
        MaxNum = max(MaxNum, curNum)
        return

    for tx, ty in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty]:

            dfs(tx, ty, visited, cnt+1, curNum)
            visited[tx][ty] = False


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
visited = [[False for d in range(M)] for i in range(N)]
MaxNum = 0


for i in range(N):
    for d in range(M):
        MaxNum = max(MaxNum, calExShape(i, d))

for i in range(N):
    for d in range(M):
        dfs(i, d, visited, 1, 0)
        visited[i][d] = False

print(MaxNum)
