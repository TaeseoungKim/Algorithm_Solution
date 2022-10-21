# 수정 필요
import sys
from collections import deque
input = sys.stdin.readline


def dfs(cur, time):
    global maxV
    if cur == W:
        # maxV = max(maxV, time+Times[cur-1])
        return

    for edge in edges[cur]:
        newTime = time+Times[edge-1]
        if maxArr[edge] < newTime:
            maxArr[edge] = newTime
            dfs(edge, newTime)


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    Times = list(map(int, input().split()))
    edges = [[] for i in range(N+1)]
    checks = [False for i in range(N+1)]
    checks[0] = True
    maxArr = [0 for i in range(N+1)]
    maxV = 0

    for i in range(K):
        t1, t2 = map(int, input().split())
        edges[t1].append(t2)
        checks[t2] = True
    # edges 연결된게 없는거를 시작점으로 잡는다.

    S = checks.index(False)
    W = int(input())
    if checks[W] == False:
        print("정답", Times[W-1])
        continue
    dfs(S, Times[S-1])
    print("정답", maxArr[W])
