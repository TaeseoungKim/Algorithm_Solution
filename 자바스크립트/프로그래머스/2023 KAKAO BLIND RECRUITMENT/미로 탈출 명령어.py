import sys
sys.setrecursionlimit(5000)

n = 2
m = 2
x = 1
y = 1
r = 2
c = 2
k = 2

# l: 왼쪽으로 한 칸 이동
# r: 오른쪽으로 한 칸 이동
# u: 위쪽으로 한 칸 이동
# d: 아래쪽으로 한 칸 이동


def bfs(n, m, board, cnt, path, x, y, r, c, result, k):
    if result and path[0] > result[0][0]:
        return
    if cnt == k:
        if x == r and y == c:
            result.append(path)
            result.sort()
            return
        else:
            return

    for tx, ty, direction in [(x+1, y, "d"),  (x, y-1, "l"), (x, y+1, "r"), (x-1, y, "u")]:
        if 0 <= tx < n and 0 <= ty < m:
            bfs(n, m, board, cnt+1, path+direction, tx, ty, r, c, result, k)


def solution(n, m, x, y, r, c, k):
    board = [[False for _ in range(m)] for _ in range(n)]
    board[x-1][y-1] = "START"
    board[r-1][c-1] = "END"
    distance = abs(r-x) + abs(c-y)
    if k < distance:
        return "impossible"
    if (k-distance) % 2 == 1:
        return "impossible"

    result = []
    bfs(n, m, board, 0, "", x-1, y-1, r-1, c-1, result, k)
    result.sort()
    if len(result) > 0:
        return result[0]
    else:
        return "impossible"


print(solution(n, m, x, y, r, c, k))
