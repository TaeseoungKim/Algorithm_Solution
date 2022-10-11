import imp
import sys
import copy
deepcopy = copy.deepcopy
input = sys.stdin.readline


N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for i in range(N)]
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.


for i in range(N):
    print(board[i])

houseInfo = []
chickenInfo = []

for i in range(N):
    for d in range(N):
        if board[i][d] == 1:
            houseInfo.append([i, d])
        elif board[i][d] == 2:
            chickenInfo.append([i, d])

houseCnt = len(houseInfo)
chickenCnt = len(chickenInfo)
close = chickenCnt-M

print(close, chickenCnt)

visited = [False for i in range(chickenCnt)]
minDist = sys.maxsize
print("close", close)

count = 0


def recursion(visited, close):
    global count

    print("count", count)
    print("visited", visited)
    if count == 3000:
        return

    print("\nrecursion 호출:", close)
    global minDist
    if close == 0:
        CityDist = 0
        for i in range(houseCnt):
            chickenDist = sys.maxsize
            for d in range(chickenCnt):
                if visited[d] == False:  # 닫은 가게가 아닐 경우만
                    hy, hx = houseInfo[i]
                    cy, cx = chickenInfo[d]
                    chickenDist = min(chickenDist, abs(hy-cy) + abs(hx-cx))
            CityDist += chickenDist
        print("minDist", minDist)
        minDist = min(minDist, CityDist)
        return

    print("chickenCnt", chickenCnt)
    count += 1

    for i in range(chickenCnt):
        if visited[i] == False:
            visited[i] = True
            recursion(deepcopy(visited), close-1)
            visited[i] = False


recursion(visited, close)
print(minDist)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
