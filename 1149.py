import sys

n = int( sys.stdin.readline() )
board = [ list(map(int,sys.stdin.readline().split()) ) for _ in range(n) ]

M = 0
for i in range(1,n):
    board[i][0] = min(board[i-1][1],board[i-1][2]) + board[i][0]
    board[i][1] = min(board[i-1][0],board[i-1][2]) + board[i][1]
    board[i][2] = min(board[i-1][0],board[i-1][1]) + board[i][2]

print(min(board[n-1]))