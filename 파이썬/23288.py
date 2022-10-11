import sys
from collections import deque

input = sys.stdin.readline
N, M, K = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dice = [2, 1, 5, 6, 4, 3]
curDir = 1
curPos = [0, 0]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def printDice():
    print(" ", dice[0])
    print(dice[4], dice[1], dice[5])
    print(" ", dice[2])
    print(" ", dice[3])


def moveDir(dir):
    global curDir
    if dir == "left":  # 시계
        if curDir == 4:
            curDir = 1
        else:
            curDir += 1
    elif dir == "right":  # 반시계
        if curDir == 1:
            curDir = 4
        else:
            curDir -= 1


def moveDice(dir):
    global curPos, dice, curDir

    if dir == 1:  # right
        if curPos[1] == M-1:
            moveDice(3)
            curDir = 3
            return
        dice[5], dice[4], dice[1], dice[3] = dice[1], dice[3], dice[4], dice[5]
        curPos = [curPos[0], curPos[1]+1]
        return
    elif dir == 2:  # bottom
        if curPos[0] == N-1:
            moveDice(4)
            curDir = 4
            return
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
        curPos = [curPos[0]+1, curPos[1]]
        return
    if dir == 3:  # left
        if curPos[1] == 0:
            moveDice(1)
            curDir = 1
            return
        dice[4], dice[5], dice[1], dice[3] = dice[1], dice[3], dice[5], dice[4]
        curPos = [curPos[0], curPos[1]-1]
        return
    elif dir == 4:  # top
        if curPos[0] == 0:
            moveDice(2)
            curDir = 2
            return
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
        curPos = [curPos[0]-1, curPos[1]]
        return


def bfs():
    global dice, curPos
    queue = deque()
    queue.append(curPos)
    Cnt = 1
    visited = []
    for _ in range(N):
        visited.append([False for i in range(M)])
    visited[curPos[0]][curPos[1]] = True

    while queue:
        curY, curX = queue.popleft()
        for dy, dx in [[curY+1, curX], [curY, curX+1], [curY-1, curX], [curY, curX-1]]:
            if 0 <= dy < N and 0 <= dx < M and visited[dy][dx] != True:
                visited[dy][dx] = True
                if board[dy][dx] == board[curPos[0]][curPos[1]]:
                    Cnt += 1
                    queue.append([dy, dx])
    return Cnt


answer = 0

for i in range(K):
    moveDice(curDir)
    if board[curPos[0]][curPos[1]] < dice[3]:
        moveDir("left")
    elif board[curPos[0]][curPos[1]] > dice[3]:
        moveDir("right")
    elif board[curPos[0]][curPos[1]] == dice[3]:
        pass

    tmpbfs = bfs()
    answer += tmpbfs * board[curPos[0]][curPos[1]]

print(answer)
