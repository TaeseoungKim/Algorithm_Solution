import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    answer = 0
    deq = deque()
    N, K = map(int, input().split())
    timeToBuild = list(map(int, input().split())) # 0부터 시작하는 거 기억
    board = [[] for i in range(N+1)]
    degree = [0 for i in range(N+1)]
    visited = [0 for i in range(N+1)]
    for d in range(K):
        X, Y = map(int, input().split())
        board[X].append(Y)
        degree[Y] += 1
    W = int(input())

    for n in range(1,N+1):
        if degree[n]==0:
            deq.append(n)
            visited[n] = timeToBuild[n-1]

    while deq:
        pNode = deq.popleft()
        answer += timeToBuild[pNode-1]
        for node in board[pNode]:
            degree[node] -= 1
            visited[node] = max(visited[node],visited[pNode]+timeToBuild[node-1]) 
            if degree[node] == 0:
                deq.append(node)

    print(visited[W])


    