import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def move(cnt, curPosition):
    global isSimple, isNotSimple, x, X, y, Y
    visited[curPosition] = True

    for t in range(4):
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)][t]
        nextPosition = (curPosition[0]+dir[0], curPosition[1]+dir[1])

        # 갈 곳이 방문했던 곳이면 종료하고 심플하지 않다.
        if nextPosition in visited:
            isNotSimple += [x, X, y, Y][t]
            continue

        if cnt-1 == 0:  # 갈 곳이 방문했던 곳이 아니므로 심플하다.
            isSimple += [x, X, y, Y][t]
            continue

        move(cnt-1, nextPosition)
        del visited[nextPosition]


N, x, X, y, Y = map(int, input().split())

visited = dict()

isSimple = 0
isNotSimple = 0

move(N, (0, 0))
print("isSimple", isSimple)
print("isNotSimple", isNotSimple)
print(isSimple/(isSimple+isNotSimple))
