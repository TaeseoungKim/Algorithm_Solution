import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
student = int(input())
order = list()


def swap(board, i):
    if board[i] == 1:
        board[i] = 0
    else:
        board[i] = 1


for i in range(student):
    sex, num = map(int, input().split())
    order.append((sex, num))

for sex, num in order:
    if sex == 1:  # 남학생
        for i in range(num-1, N, num):
            swap(board, i)
    else:
        swap(board, num-1)
        rangeToCompare = min(num-1, N-num)
        for i in range(1, rangeToCompare+1, 1):
            if board[num-1-i] == board[num-1+i]:
                swap(board, num-1-i)
                swap(board, num-1+i)
            else:
                break

cnt = 0
for i in range(N):
    cnt += 1
    print(board[i], end=" ")
    if cnt == 20:
        cnt = 0
        print()
