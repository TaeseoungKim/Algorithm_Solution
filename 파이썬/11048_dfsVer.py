from collections import deque
import sys
input = sys.stdin.readline

move = [[1,0],[0,1],[1,1]]
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]
result[0][0] = board[0][0]
deq = deque()
deq.append((0,0))
while deq:
    cur_x, cur_y = deq.pop()
    for next_x, next_y in move:
        if not(0<= cur_x+next_x <n and 0<= cur_y+next_y <m):
                continue
        if result[cur_x+next_x][cur_y+next_y]==0 or result[cur_x+next_x][cur_y+next_y] < board[cur_x+next_x][cur_y+next_y]+result[cur_x][cur_y]:
            result[cur_x+next_x][cur_y+next_y] = board[cur_x+next_x][cur_y+next_y]+result[cur_x][cur_y]
            deq.append((cur_x+next_x,cur_y+next_y))
print(result[n-1][m-1])