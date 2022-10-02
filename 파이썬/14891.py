from collections import deque
import sys

input = sys.stdin.readline
wheel  = []
move = []
for _ in range(4):
    wheel.append(deque(input()[:8]))
k = int(input())
for _ in range(k):
    move.append(tuple(map(int, input().split())))

cnt = 0
def wheelmove(idx,dir,LeftOrRight):
    global cnt
    cnt += 1

    # 톱니바퀴 범위를 벗어났을 때,(1~4)
    if idx == -1 or idx == 4:
        return
    if LeftOrRight == -1:
        if wheel[idx][2]!=wheel[idx+1][6]:
            wheelmove(idx-1,-dir,-1)
            wheel[idx].rotate(-dir)
    elif LeftOrRight == 1:
        if wheel[idx][6]!=wheel[idx-1][2]:
            wheelmove(idx+1,-dir,1)
            wheel[idx].rotate(-dir)

for idx, dir in move:
    wheelmove(idx-2,dir,-1)
    wheelmove(idx,dir,1)
    wheel[idx-1].rotate(dir)
    
result = 0
if wheel[0][0]=='1':
    result += 1
if wheel[1][0]=='1':
    result += 2
if wheel[2][0]=='1':
    result += 4
if wheel[3][0]=='1':
    result += 8
print(result)
