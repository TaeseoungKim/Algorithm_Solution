import sys
input = sys.stdin.readline


def checkBingo(board):
    bingoCnt = 0
    leftCnt = 0
    rightCnt = 0
    for i in range(5):
        if board[i][i] == -1:
            leftCnt += 1
        if board[4-i][i] == -1:
            rightCnt += 1

    if leftCnt == 5:
        bingoCnt += 1
    if rightCnt == 5:
        bingoCnt += 1

    for i in range(5):
        if board[i][0]+board[i][1]+board[i][2]+board[i][3]+board[i][4] == -5:
            bingoCnt += 1
        if board[0][i]+board[1][i]+board[2][i]+board[3][i]+board[4][i] == -5:
            bingoCnt += 1

    if bingoCnt >= 3:
        return True
    else:
        return False


board = [list(map(int, input().split())) for i in range(5)]
numberSeq = [list(map(int, input().split())) for i in range(5)]

posDict = dict()

for i in range(1, 25, 1):
    posDict[i] = 0

for i in range(5):
    for d in range(5):
        posDict[board[i][d]] = (i, d)

Bingo = 0
callCnt = 0
for i in range(5):
    for d in range(5):
        callCnt += 1
        x, y = posDict[numberSeq[i][d]]
        board[x][y] = -1
        if checkBingo(board):
            print(callCnt)
            callCnt = -1
            break
        else:
            continue
    if callCnt == -1:
        break
