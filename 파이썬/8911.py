from collections import deque
import sys
input = sys.stdin.readline


def moveY():
    global curY
    if Yaxis[-1] > curY:
        curY += 1
    elif Yaxis[-1] == curY:
        curY += 1
        Yaxis.append(curY)


def moveYreverse():
    global curY
    if Yaxis[0] < curY:
        curY -= 1
    elif Yaxis[0] == curY:
        curY -= 1
        Yaxis.appendleft(curY)


def moveX():
    global curX
    if Xaxis[-1] > curX:
        curX += 1
    elif Xaxis[-1] == curX:
        curX += 1
        Xaxis.append(curX)


def moveXreverse():
    global curX
    if Xaxis[0] < curX:
        curX -= 1
    elif Xaxis[0] == curX:
        curX -= 1
        Xaxis.appendleft(curX)


testCase = int(input())
move = ["+Y", "+X", "-Y", "-X"]

for t in range(testCase):
    Xaxis, Yaxis = deque([0]), deque([0])
    curX, curY = 0, 0
    curDirection = 0

    opCode = input()
    for op in opCode:

        if op == "F":
            if move[curDirection] == "+Y":
                moveY()
            elif move[curDirection] == "-Y":
                moveYreverse()
            elif move[curDirection] == "+X":
                moveX()
            elif move[curDirection] == "-X":
                moveXreverse()

        elif op == "B":
            if move[curDirection] == "+Y":
                moveYreverse()
            elif move[curDirection] == "-Y":
                moveY()
            elif move[curDirection] == "+X":
                moveXreverse()
            elif move[curDirection] == "-X":
                moveX()

        elif op == "L":
            if curDirection == 0:
                curDirection = 3
            else:
                curDirection -= 1

        elif op == "R":
            if curDirection == 3:
                curDirection = 0
            else:
                curDirection += 1
    result = (len(Xaxis)-1)*(len(Yaxis)-1)
    print(result)
