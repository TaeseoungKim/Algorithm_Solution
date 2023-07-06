import sys
input = sys.stdin.readline

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]
curX, curY, curDir = map(int, input().split())
for i in range(N):
    inputLine = list(map(int, input().split()))
    for d in range(M):
        board[i][d] = inputLine[d]


answer = 0
while True:
    if board[curX][curY] == 0:
        board[curX][curY] = -1
        answer += 1

    isAllCleared = True
    for pX, pY in move:
        nextX, nextY = curX+pX, curY+pY
        if 0 <= nextX < N and 0 <= nextY < M and board[nextX][nextY] == 0:
            isAllCleared = False

    if isAllCleared:
        pX, pY = move[curDir]
        pX *= -1
        pY *= -1
        if 0 <= curX+pX < N and 0 <= curY+pY < M and board[curX+pX][curY+pY] != 1:
            curX = curX+pX
            curY = curY+pY
            continue
        else:
            break
    else:
        if curDir == 0:
            curDir = 3
        else:
            curDir -= 1
        pX, pY = move[curDir]
        if board[curX+pX][curY+pY] == 0:
            curX = curX+pX
            curY = curY+pY
print(answer)
