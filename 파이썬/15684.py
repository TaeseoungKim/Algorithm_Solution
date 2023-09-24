import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[False for _ in range(N)] for _ in range(H)]

for i in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = True


def checkSuccess():
    for i in range(N):
        curCol = i
        for d in range(H):
            if ladder[d][curCol]:  # 우로 이동
                curCol += 1
            elif curCol > 0 and ladder[d][curCol-1]:  # 좌로 이동
                curCol -= 1
        if curCol != i:
            return False
    return True


def dfs(cnt, x, y):
    global ans
    if checkSuccess():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, H):
        if i == x:
            col = y
        else:
            col = 0

        for d in range(col, N-1):
            if not ladder[i][d] and not ladder[i][d+1]:
                if d > 0 and ladder[i][d - 1]:
                    continue
                ladder[i][d] = True
                dfs(cnt+1, i, d+2)
                ladder[i][d] = False


ans = 4
if M == 0:
    print(0)
else:
    dfs(0, 0, 0)
    print(ans if ans < 4 else -1)
