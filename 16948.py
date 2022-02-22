from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
board = [[0]*n for _ in range(n)]
move = [(-2, -1), (-2, 1), (0, -2), (0, +2), (2, -1), (2, 1)]


def bfs():
    deq = deque()
    deq.append((x1,y1))
    while deq:
        x,y=deq.popleft()
        if x==x2 and y==y2:
            break
        for tx,ty in move:
            if 0<= x+tx <n and 0<= y+ty <n:
                if board[x+tx][y+ty]==0:
                    deq.append((x+tx,y+ty))
                    board[x+tx][y+ty] += board[x][y]+1    
bfs()
if board[x2][y2]==0:
    print(-1)
else:print(board[x2][y2])