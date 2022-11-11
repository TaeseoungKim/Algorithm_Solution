
import sys
input = sys.stdin.readline
T = int(input())
answer = 0
for i in range(T):
    board = input().rstrip()
    newSet = set(board)
    for idx, c in enumerate(board):
        if idx == 0 or board[idx] != board[idx-1]:
            if board[idx] in newSet:
                # newSet.remove
                newSet.discard(board[idx])
            else:
                continue
    else:
        answer += 1
print(answer)
