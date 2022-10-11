# 2000문제 푼 임스 실패

import sys
import itertools
import copy

deepcopy = copy.deepcopy
input = sys.stdin.readline

C = float(input())
N = int(input())
board = list(map(int, input().split(" ")))

skill = 0
if C >= 1.98:
    skill = 2
elif C >= 0.99:
    skill = 1

restDay = []
for i in range(len(board)):
    if board[i] == 0:
        restDay.append(i)

maxSeq = 0

for restDays in itertools.combinations(restDay, skill):
    newBoard = deepcopy(board)
    seqArray = [0]
    seq = 0
    for day in restDays:
        newBoard[day] = -1
    for i in range(N):
        if newBoard[i] != 0:
            seq += 1
            if i == N-1:
                seqArray.append(seq)
        else:
            seqArray.append(seq)
            seq = 0

    maxSeq = max(maxSeq, max(seqArray))

print(maxSeq)
print(max(board))
