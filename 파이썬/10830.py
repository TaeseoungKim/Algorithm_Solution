import sys
from copy import copy, deepcopy
from collections import deque

input = sys.stdin.readline
N, B = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for i in range(N)]


visited = {}
visited[1] = board
tempArr = deque()


def mul(arr1, arr2, len1, len2):
    keyNum = len1+len2
    if keyNum in visited:
        return visited[keyNum]

    answer = [len(arr2[0])*[0] for i in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            answer[i][j] %= 1000
    visited[keyNum] = answer
    return answer


count = 0


def sol(Num):
    global count
    if count == 10:
        return
    count += 1

    if Num in visited:
        return visited[Num]
    if Num % 2 != 0:
        tempArr.append(1)
        Num -= 1
        return mul(sol(Num//2), sol(Num//2), Num//2, Num//2)
    else:
        return mul(sol(Num//2), sol(Num//2), Num//2, Num//2)


newBoard = sol(B)
while tempArr:
    tempArr.pop()
    newBoard = mul(newBoard, visited[1])

for i in range(len(newBoard)):
    print(*newBoard[i])
