import sys

n = int(sys.stdin.readline())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
number = [ [0] * n for _ in range(n)]
number[0][0] = 1

for y in range(n):
    for x in range(n):
        if number[y][x] != 0 and board[y][x] != 0:
            if y + board[y][x] < n:
                number[y + board[y][x] ][x] += number[y][x]
            if x + board[y][x] < n:
                number[y][x + board[y][x]] += number[y][x]

print(number[n-1][n-1])