import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    minDist = [sys.maxsize for _ in range(v+1)]
    minDist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        curDist, pNode = heapq.heappop(heap)
        if minDist[pNode] < curDist:
            continue
        for nextNode, nextCost in graph[pNode]:
            if minDist[nextNode] > curDist+nextCost:
                minDist[nextNode] = curDist+nextCost
                heapq.heappush(heap, (curDist+nextCost, nextNode))

    return minDist

answer = 0
backDist = dijkstra(x)
for i in range(1,v+1):
    minDist = dijkstra(i)
    answer = max(answer, minDist[x]+backDist[i])
print(answer)