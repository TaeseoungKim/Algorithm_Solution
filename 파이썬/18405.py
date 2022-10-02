from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [ 0 for _ in range(N) ]
for _ in range(N):
    board[_] = list(map(int, input().split()))
S, X, Y = map(int, input().split())
deq = deque([deque() for _ in range(K)] )

move = [(0,1),(0,-1),(-1,0),(1,0)] 

for y in range(N):
    for x in range(N):
        if board[y][x] != 0:    
            deq[board[y][x]-1].append((x,y))

def bfs(K,S,X,Y):
    sec = 0
    while deq:
        if sec >= S:
            print(board[Y][X])
            break
        
        for d in range(K):
            for i in range(len(deq[d])):
                x,y = deq[d].popleft()
                
                for tmp_x, tmp_y in move:
                    #범위를 벗어날 시 continue
                    if not(x+tmp_x >= 0 and x+tmp_x < N and y+tmp_y >= 0 and y+tmp_y < N) :
                        continue
                    if board[y+tmp_y][x+tmp_x] == 0:
                        deq[d].append((x+tmp_x,y+tmp_y))
                        board[y+tmp_y][x+tmp_x] = board[y][x]
                    
        sec += 1
                    
bfs(K,S,Y-1,X-1)