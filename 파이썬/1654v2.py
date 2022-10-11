import sys
input = sys.stdin.readline
K, N = map(int, input().split(" "))
board = []

for i in range(K):
    board.append(int(input()))

left = 1
right = max(board)
answer = []


def binarySearch(left, right):
    global N, K, answer
    mid = (left+right)//2
    sumV = 0
    for i in range(K):
        sumV += board[i]//mid

    if left > right:
        answer.append(mid)
    elif sumV >= N:
        answer.append(mid)
        binarySearch(mid+1, right)
    elif sumV < N:
        binarySearch(left, mid-1)


binarySearch(left, right)
print(max(answer))
