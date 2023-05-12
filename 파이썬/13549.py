from collections import deque
N, K = map(int, input().split())

MAX_SIZE = 100001
board = [-1 for i in range(MAX_SIZE)]
board[N] = 0
queue = deque()
queue.append(N)

while queue:
    px = queue.popleft()
    if px == K:
        print(board[K])
        break

    if 0 <= px-1 < MAX_SIZE and board[px-1] == -1:
        board[px-1] = board[px]+1
        queue.append(px-1)
    if 0 < px*2 < MAX_SIZE and board[px*2] == -1:
        board[px*2] = board[px]
        queue.appendleft(px*2)
    if 0 <= px+1 < MAX_SIZE and board[px+1] == -1:
        board[px+1] = board[px]+1
        queue.append(px+1)
