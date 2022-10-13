from itertools import combinations, permutations
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split(" ")))
edges = []

for i in range(N):
    inputs = list(map(int, input().split(" ")))
    edges.append(inputs[1:])


# def connected(team):
people = list(range(N))


def bfs(team):
    queue = deque()
    queue.append(team[0])
    peopleCnt = board[team[0]]
    numberCheck = 1

    visited = [False for i in range(N)]
    visited[team[0]] = True
    while queue:
        idx = queue.popleft()
        for node in edges[idx]:
            node -= 1

            if node in team and not visited[node]:
                queue.append(node)
                peopleCnt += board[node]
                numberCheck += 1
            visited[node] = True
    return peopleCnt, numberCheck


MinV = sys.maxsize

for i in range(1, N//2+1):
    redTeams = list(combinations(range(N), i))
    for redTeam in redTeams:

        blueTeam = [i for i in range(N) if not i in redTeam]

        redPeopleCnt, redNumberCheck = bfs(redTeam)
        bluePeopleCnt, blueNumberCheck = bfs(blueTeam)
        if redNumberCheck == len(redTeam) and blueNumberCheck == len(blueTeam):
            MinV = min(abs(redPeopleCnt-bluePeopleCnt), MinV)

if MinV == sys.maxsize:
    print(-1)
else:
    print(MinV)
