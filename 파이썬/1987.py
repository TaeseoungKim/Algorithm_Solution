import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

minDist = 0
alphaDict = dict()


def backTracking(pos, pathCnt):
    global minDist
    minDist = max(minDist, pathCnt)

    x = pos[0]
    y = pos[1]

    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alphaDict:
            alphaDict[board[nx][ny]] = True
            backTracking((nx, ny), pathCnt+1)
            del alphaDict[board[nx][ny]]


alphaDict[board[0][0]] = True
backTracking((0, 0), 1)
print(minDist)
