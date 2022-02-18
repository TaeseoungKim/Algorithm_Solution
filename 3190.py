from collections import deque
import sys
input = sys.stdin.readline

#보드크기, 사과개수
n = int(input())
k = int(input())
board = list([0]*n for _ in range(n) )
# 뱀의 시작 위치
board[0][0] = 1

for _ in range(k):
    y,x = map(int, input().split())
    board[y][x] = 2
l = int(input())
snake_move = deque()

for _ in range(l):
    time, direction = input().split()
    snake_move.append((int(time),direction))

#상우하좌 (시계방향), 현재 방향
move = [(-1,0), (0,1), (1,0), (0,-1)]
cur_dir = 1
# 시간초, 뱀의 머리/꼬리
cnt=0
head = [0,0]
tail = [0,0]
gameover=0

for _ in range(len(snake_move)):
    time, direction = snake_move.popleft()
    while True:


        cnt += 1
        if time==cnt:
            if direction=='L':
                if cur_dir == 0:
                    cur_dir = 3
                else: cur_dir -= 1

            elif direction=='D':
                if cur_dir == 3:
                    cur_dir = 0
                else: cur_dir += 1
            cnt -= 1
            break

        head[0] += move[cur_dir][0]
        head[1] += move[cur_dir][1]

        if not(0 <= head[0] < n) or not(0 <= head[1] < n) or (board[head[0]][head[1]] == 1):
            print(cnt+1)
            gameover = 1
            break
        elif board[head[0]][head[1]] == 2:
            board[head[0]][head[1]] = 1
        
        else: 
            board[head[0]][head[1]] = 1
            board[tail[0]][tail[1]] = 0
        
            tail[0] += move[cur_dir][0]
            tail[1] += move[cur_dir][1]

    if gameover==1:
        break
