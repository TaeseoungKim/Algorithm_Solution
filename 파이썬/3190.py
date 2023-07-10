import sys
from collections import deque
input = sys.stdin.readline
SPACE, APPLE = 0,1 # 0 보드, 1 사과

boardLen = int(input())
appleCnt = int(input())
apples = []
for i in range(appleCnt):
    x,y = map(int, input().split())
    apples.append((x-1,y-1))

bites = []

moveCnt =  int(input())
moveQueue = deque()
for i in range(moveCnt):
    x,c = input().split()
    x = int(x)
    moveQueue.append((x,c))

moveDirection = [(0,1),(1,0),(0,-1),(-1,0)]
curMove = 0

sneakQueue = deque()
curHead = (0,0)
sneakQueue.append(curHead)

curTime = 0


def isEnd(x,y):
    if not (0<=x<boardLen and 0<=y<boardLen):
        return True
    if (x,y) in sneakQueue:
        return True
        
        

while True:
    curX,curY = curHead

    if moveQueue:
        pTime, pMove = moveQueue[0]
        if pTime==curTime:
            moveQueue.popleft()
            if pMove=="L":
                if curMove==0:
                    curMove=3
                else:
                    curMove -= 1
            elif pMove=="D":
                if curMove==3:
                    curMove=0
                else:
                    curMove += 1
    
    nextX, nextY = curX+moveDirection[curMove][0],curY+moveDirection[curMove][1]

    if isEnd(nextX,nextY):
        curTime+=1
        break
    else:
        if (nextX, nextY) in apples and (nextX, nextY) not in bites:      
            sneakQueue.appendleft((nextX,nextY))
            bites.append((nextX, nextY))

        else:
            sneakQueue.appendleft((nextX,nextY))
            sneakQueue.pop()
        curHead = (nextX, nextY)
    
    curTime+=1

print(curTime)