import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x,y):
    deq = deque()
    deq.append((y,x))

    while deq:
        pop_y, pop_x = deq.popleft()
        board[pop_y][pop_x] = 0
        for next_y, next_x in [(pop_y+1,pop_x),(pop_y-1,pop_x),(pop_y,pop_x+1),(pop_y,pop_x-1)]:
            if 0 <= next_y < m and 0 <= next_x < n:
                if board[next_y][next_x] == 1:
                    deq.append((next_y,next_x))

t = int(input())
count = []

for i in range(t):
    temp = 0
    n,m,k = map(int,input().split())
    board = [[0]*n for i in range(m)]
    for j in range(k):
        x, y = map(int,input().split())
        board[y][x] = 1

    for x in range(n):
        for y in range(m):
            if board[y][x] == 1:
                temp += 1
                dfs(x,y)
    count.append(temp)

for c in count:
    print(c)