import sys
from collections import deque

input = sys.stdin.readline
testCase = int(input())
myStack = deque()
for t in range(testCase):
    board = input().split()
    op = board[0]

    if op == "pop":
        if len(myStack) == 0:
            print(-1)
            continue
        print(myStack.pop())
    elif op == "size":
        print(len(myStack))
    elif op == "empty":
        if len(myStack) == 0:
            print(1)
        else:
            print(0)
    elif op == "top":
        if len(myStack) == 0:
            print(-1)
            continue
        print(myStack[-1])
    elif op == "push":
        myStack.append(board[1])
