import copy
import sys
from collections import deque

input = sys.stdin.readline

# 물고기 냄새, 상어가 있는 칸을 담는 배열


smellBoard = [list([deque(), deque(), deque(), deque(), deque()])
              for i in range(5)]
fishBoard = [list([deque(), deque(), deque(), deque(), deque()])
             for i in range(5)]

M, S = map(int, input().split(" "))
for i in range(M):
    fx, fy, d = map(int, input().split(" "))
    fishBoard[fx][fy].append(d)
sx, sy = map(int, input().split(" "))
# f[sx][sy] = -1
sharkPos = [sx, sy]

move = [(0, 0), (-1, 0), (-1, -1), (0, -1),
        (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def printBoard(board):
    print()
    print()
    boardLen = len(board)
    for i in range(boardLen):
        for d in range(len(board[i])):
            while board[i][d]:
                tmp = board[i][d].pop()
                print(tmp, ",", end="")
        print()


def deleteFishSmell():
    return


def FishMove(fishBoard, smellBoard, sharkPos):
    [sx, sy] = sharkPos

    for dx in range(1, 5):
        for dy in range(1, 5):
            for _ in range(len(fishBoard[dx][dy])):
                curDir = fishBoard[dx][dy][0]
                cnt = 0
                while True:
                    newDir = (curDir+cnt) % 8
                    mx, my = move[newDir]
                    if cnt == 8:
                        break
                    if 1 <= dx+mx <= 4 and 1 <= dy+my <= 4 and len(smellBoard[dx+mx][dy+my]) == 0 and not (dx+mx == sx and dy+my == sy):
                        fishBoard[dx+mx][dy+my].append(fishBoard[dx][dy][0])
                        cnt = -1
                        break
                    cnt += 1
                if cnt == -1:
                    fishBoard[dx][dy].popleft()
                else:
                    fishBoard[dx][dy].append(fishBoard[dx][dy].popleft())

    return fishBoard


answer = []


def SharkMove(sharkPos, S, moveCnt, path, smellBoard, fishBoard, visited):
    printBoard(fishBoard)
    if moveCnt == 5:
        return
    newFishBoard = copy.deepcopy(fishBoard)
    visited[sharkPos[0]][sharkPos[1]] = True

    if moveCnt % 3 == 0 and moveCnt != 0:
        moveCnt = 0
        newFishBoard = FishMove(copy.deepcopy(fishBoard), smellBoard, sharkPos)
        visited = [list([False, False, False, False, False])
                   for i in range(5)]
        visited[sharkPos[0]][sharkPos[1]] = True
        S -= 1
        for dx in range(1, 5):
            for dy in range(1, 5):
                while smellBoard[dx][dy]:
                    tmp = smellBoard[dx][dy].pop()
                    tmp -= 1
                    if tmp == 0:
                        break
                    smellBoard[dx][dy].append(tmp)

    if S == 0:
        sum = 0
        for dx in range(1, 5):
            for dy in range(1, 5):
                sum += len(newFishBoard[dx][dy])
        answer.append(path+"답"+str(sum))
        return

    px, py = sharkPos
    for tx, ty, p in [(px+1, py, 4), (px, py+1, 3), (px-1, py, 2), (px, py-1, 1)]:
        if 1 <= tx <= 4 and 1 <= ty <= 4 and not visited[tx][ty]:
            visited[tx][ty] = True
            moveCnt += 1
            sharkPos = [tx, ty]
            newPath = path+str(p)

            if newFishBoard[tx][ty]:
                newFishBoard[tx][ty] = deque()
                smellBoard[tx][ty].append(2)

            if moveCnt % 3 == 0 and moveCnt != 0:
                for dx in range(1, 5):
                    for dy in range(1, 5):
                        while fishBoard[dx][dy]:
                            newFishBoard[dx][dy].append(
                                fishBoard[dx][dy].pop())

            SharkMove([tx, ty], S, moveCnt, newPath, copy.deepcopy(
                smellBoard), copy.deepcopy(newFishBoard), visited)


visited = [list([False, False, False, False, False])
           for i in range(5)]
SharkMove(copy.deepcopy(sharkPos), S, 0, "", copy.deepcopy(
    smellBoard), copy.deepcopy(fishBoard), copy.deepcopy(visited))

print(answer)
