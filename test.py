from collections import deque

# board = [[1],[2],[3],[4],[5]]
# i=1
# temp = [*board[1:]]
# print(temp)
# temp[1]=100
# print(board)
# print(temp)

n=int(input())
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))
i=1
print(board)
print([*board[:i],[board[i][0],board[i+1][1]],*board[i+2:]])