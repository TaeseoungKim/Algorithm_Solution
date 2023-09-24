import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
tempBoard = [list(map(int, input().split())) for _ in range(N)]
board = []

for i in range(N):
    board.append([])
    for d in range(N):
        board[i].append([tempBoard[i][d], tempBoard[i][d]])  # 현재체력, 초기체력


bullets = list(map(int, input().split()))

colLen = len(board)
rowLen = len(board[0])

answer = 0


def makeTarget(x, y, board):
    originValue = [board[x][y][0], board[x][y][1]]
    madePos = []
    for nx, ny in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if 0 <= nx < colLen and 0 <= ny < rowLen and board[nx][ny][0] == 0:
            board[nx][ny] = [board[x][y][1] // 4, board[x][y][1] // 4]
            madePos.append((nx, ny))
    board[x][y] = [0, 0]
    return [originValue, madePos]


def removeTarget(x, y, originValue, madePos):
    for nx, ny in madePos:
        board[nx][ny] = [0, 0]
    board[x][y] = [originValue[0], originValue[1]]


cnt = 0


def isEmpty(col):
    for i in range(rowLen):
        if board[col][i][0] != 0:
            return False
    else:
        return True


def backTracking(col, bulletIdx, curGrade):
    global answer
    if bulletIdx == len(bullets):
        answer = max(answer, curGrade)
        return

    for i in range(rowLen):
        if board[col][i][1] >= 10:
            for nextCol in range(col, colLen):
                if not isEmpty(nextCol):
                    originHP = [board[col][i][0], board[col][i][1]]
                    board[col][i] = [0, 0]
                    backTracking(nextCol, bulletIdx+1,
                                 curGrade+originHP[1])
                    board[col][i] = [originHP[0], originHP[1]]
            break

        elif board[col][i][0] > bullets[bulletIdx]:
            for nextCol in range(col, colLen):
                if not isEmpty(nextCol):
                    board[col][i][0] -= bullets[bulletIdx]
                    backTracking(nextCol, bulletIdx+1, curGrade)
                    board[col][i][0] += bullets[bulletIdx]
            break

        elif board[col][i][1] != 0 and board[col][i][0] <= bullets[bulletIdx]:
            for nextCol in range(col, colLen):
                if not isEmpty(nextCol):
                    [originValue, madePos] = makeTarget(col, i, board)
                    backTracking(nextCol, bulletIdx+1,
                                 curGrade+originValue[1])
                    removeTarget(col, i, originValue, madePos)
            break


for col in range(0, colLen):
    if not isEmpty(col):
        backTracking(col, 0, 0)
print(answer)
