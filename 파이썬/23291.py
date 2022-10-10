import sys
from collections import deque
input = sys.stdin.readline


def printBowl(board, ment=""):
    N = len(board)
    print("\n\n", ment)
    for i in range(N):
        print(board[i])


N, K = map(int, input().split(" "))

board = [[0 for d in range(N+1)]for i in range(N+1)]
fishBowl = list(map(int, input().split(" ")))
for i in range(N):
    board[N][i+1] = fishBowl[i]

# 2phase
minFish = min(board[N][1:])
for i in range(N):
    if board[N][i+1] == minFish:
        board[N][i+1] += 1

count = 1
세로 = 1
가로 = 1
while True:
    if count % 2 == 0:
        세로 += 1

    # 공중부양
    공중부양 = [[0 for i in range(가로)] for d in range(세로)]
    for sero in range(세로):
        for garo in range(가로):
            print("\n\n돈다잉")
            print(N, 세로, 가로, sero, garo)
            print(N-세로+1+sero, 1+garo)
            print("뭐시여", board[N-세로+1+sero][1+garo])
            공중부양[sero][garo] = board[N-세로+1+sero][1+garo]
            board[N-세로+1+sero][1+garo] = 0
    count += 1

    printBowl(공중부양, "공중부양")

    회전된공중부양 = [[0 for i in range(세로)] for d in range(가로)]
    # 공중부양한것 회전
    for sero in range(세로):
        for garo in range(가로):
            print("인포메이션: ", sero, garo, 세로-1-sero)
            회전된공중부양[sero][garo] = 공중부양[garo][세로-1-sero]

    printBowl(회전된공중부양, "회전된공중부양")
    회전된가로 = 세로
    회전된세로 = 가로

    for sero in range(회전된세로):
        for garo in range(회전된가로):
            board[N-회전된세로+sero][1+(가로*세로)+garo] = 회전된공중부양[sero][garo]

    printBowl(board, "board")
    print("-------------------------------------")

    if count == 4:
        printBowl(공중부양, "공중부양")
        break

printBowl(board)

# 세로 = 1
# 가로 = 1

# 세로 = 2 (+1)
# 가로 = 1

# 세로 = 2
# 가로 = 2 (+1)

# 세로 = 3 (+1)
# 가로 = 2


# 8 7
# 5 2 3 14 9 2 11 8
# # 3phase
# for i in range(1, N+1):
#     board


# board[N-1][2], board[N][1] = board[N][1], 0
# printBowl(board)
