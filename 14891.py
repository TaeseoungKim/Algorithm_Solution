import sys
from collections import deque

input = sys.stdin.readline

wheel = []
for _ in range(4):
    wheel.append(deque(list(input()[:8])))
k = int(input())
move = []
for _ in range(k):
    move.append(list(map(int,input().split())))
print(wheel)
print(move)
for m, dir in move:
    print(m,dir)
    if m in (1,2):
        if wheel[m-2][2] != wheel[m-1][6]:
            wheel[m-2].rotate(-dir)
        if wheel[m][6] != wheel[m-1][2]:
            wheel[m].rotate(-dir)
    if m==1:
        if wheel[m-1][2] != wheel[m+1][6]:
            wheel[m+1].rotate(-dir)




    
        