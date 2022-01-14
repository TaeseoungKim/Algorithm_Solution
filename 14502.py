import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [0]*N
for _ in range(N):
    lab[_] = list(map(int, input().split()))

for _ in range(N):
    print(lab[_])
    

def bfs():
    deq = deque()
    for y in range(N):
        for x in range(M):
            if lab[y][x]==2:
                deq.append((y,x))
                while deq:
                    pop_y, pop_x = deq.popleft()
                    
                    #상하좌우
                    if pop_y+1 < N and lab[pop_y+1][pop_x] == 0:
                        deq.append((pop_y+1,pop_x))        
                        lab[pop_y+1][pop_x] = 2
                    elif pop_y-1 >= 0 and lab[pop_y-1][pop_x] == 0:
                        deq.append((pop_y-1,pop_x))
                        lab[pop_y-1][pop_x] = 2
                    elif pop_x+1 < M and lab[pop_y][pop_x+1] == 0:
                        deq.append((pop_y,pop_x+1))
                        lab[pop_y][pop_x+1] = 2
                    elif pop_x-1 >= 0 and lab[pop_y][pop_x-1] == 0:    
                        deq.append((pop_y,pop_x-1))
                        lab[pop_y][pop_x-1] = 2
                    
                    
                    
                    
                    
    
    return
