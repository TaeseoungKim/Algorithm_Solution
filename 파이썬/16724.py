import sys
input = sys.stdin.readline

board = []
row, column = map(int, input().split())
for _ in range(row):
    board.append(input().rsplit())

print(board)
