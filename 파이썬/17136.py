import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
minPaper = sys.maxsize
myPaper = dict({1: 5, 2: 5, 3: 5, 4: 5, 5: 5, })


def findStartPoint():
    for i in range(10):
        for d in range(10):
            if board[i][d] == 1:
                return (i, d)
    return False


def checkPossible(x, y, size):
    for nx in range(x, x+size):
        for ny in range(y, y+size):
            if not (0 <= nx < 10 and 0 <= ny < 10):
                return False
            if board[nx][ny] == 0:
                return False
    return True


def attachPaper(x, y, size):
    if myPaper[size] <= 0:
        return False
    else:
        myPaper[size] -= 1
        for nx in range(x, x+size):
            for ny in range(y, y+size):
                board[nx][ny] = 0
        return True


def dettachPaper(x, y, size):
    myPaper[size] += 1
    for nx in range(x, x+size):
        for ny in range(y, y+size):
            board[nx][ny] = 1


def backTracking(SP, paperCnt):
    global minPaper

    x = SP[0]
    y = SP[1]

    for num in range(1, 6):
        if checkPossible(x, y, num):
            if not attachPaper(x, y, num):
                continue
            nextSP = findStartPoint()
            if nextSP == False:
                minPaper = min(minPaper, paperCnt+1)
                dettachPaper(x, y, num)
                return
            if paperCnt+2 < minPaper:
                backTracking(nextSP, paperCnt+1)
            dettachPaper(x, y, num)


SP = findStartPoint()
if SP == False:
    print(0)
else:
    backTracking(SP, 0)
    if minPaper == sys.maxsize:
        print(-1)
    else:
        print(minPaper)
