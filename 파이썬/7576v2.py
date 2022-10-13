#  저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for i in range(N)]
#  정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

visited = [[False for d in range(M)] for i in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(pos):
    queue = deque()
    queue.append(pos)
    visited[pos[0]][pos[1]] = True

    while queue:
        tx, ty = queue.popleft()

        for dx, dy in [(tx+1, ty), (tx, ty+1), (tx-1, ty), (tx, ty-1)]:
            if (0 <= dx < N and 0 <= dy < M) and not (visited[dx][dy]):
                visited[dx][dy] = True
                if board[dx][dy] == 0:
                    board[dx][dy] = 1
                elif board[dx][dy] == 1:
                    queue.append((dx, dy))
                    goodTomatos.append((dx, dy))


def check():
    isAll = True
    for i in range(N):
        for d in range(M):
            if board[i][d] == 0:
                isAll = False
    return isAll


goodTomatos = deque()
Impossible = False
for i in range(N):
    for d in range(M):

        if board[i][d] == 0:
            isPossible = False
            for dx, dy in [(i+1, d), (i, d+1), (i-1, d), (i, d-1)]:
                if (0 <= dx < N and 0 <= dy < M) and (board[dx][dy] == 1 or board[dx][dy] == 0):
                    isPossible = True
            if not isPossible:
                Impossible = True
        elif board[i][d] == 1:
            goodTomatos.append((i, d))


if Impossible:
    print("-1")
else:
    Days = 0
    while True:
        tomatoNum = len(goodTomatos)
        visited = [[False for d in range(M)] for i in range(N)]
        if not goodTomatos:
            break
        Days += 1
        for idx in range(tomatoNum):
            i, d = goodTomatos.popleft()
            if check():
                break
            bfs((i, d))
    print(Days)
