import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [0]*N
for _ in range(N):
    lab[_] = list(map(int, input().split()))

for _ in range(N):
    print(lab[_])

deq = deque()
# 바이러스 초기 좌표 append
for i in range(N):
        for j in range(M):
            deq.append((i,j))


move = [(1,0), (-1,0), (0,-1), (0,1)]    
max_result = 0
# bfs를 한번만 사용하는 것이 아니라 여러번 사용할 것 이기 때문에 copy를 해준다
def bfs():
    global max_result
    safeZone = 0
    tmp_lab = copy.deepcopy(lab)
    tmp_deq = copy.deepcopy(deq)
    
    while tmp_deq:
        y,x = tmp_deq.popleft()
        for tmp_y, tmp_x in move:
            
            if not(x+tmp_x >= 0 and x+tmp_x < M and y+tmp_y >= 0 and y+tmp_y < N) :
                continue
            if tmp_lab[y+tmp_y][x+tmp_x] == 0:
                tmp_deq.append((y+tmp_y,x+tmp_x))
                tmp_lab[y+tmp_y][x+tmp_x] = 2
        
    for i in range(N):
        for j in range(M):
            if tmp_lab[i][j]==0:
                safeZone+=1
                
    max_result = max(max_result,safeZone)

def wall(wall_count):
    if wall_count == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    wall(wall_count+1)
                    lab[i][j] = 0
        
                
wall(0)
print(max_result)