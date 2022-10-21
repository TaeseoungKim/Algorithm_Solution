import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = list(map(int, input().split()))

left = 1
right = max(board)


while left < right:
    mid = (left+right)//2
    sumV = 0
    for tree in board:
        meter = tree-mid
        if meter <= 0:
            continue
        sumV += meter

    if sumV >= M:
        left = mid+1
    elif sumV < M:
        right = mid
print(right-1)
