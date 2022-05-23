import sys
import heapq

input = sys.stdin.readline
n = int(input())
dasom = int(input())
heap = []

for i in range(n-1):
    t = int(input())
    heapq.heappush(heap,(-t,t))

answ=0
while dasom <= heap[0][1]:
    t = heapq.heappop(heap)[1]-1
    dasom+=1
    answ+=1
    heapq.heappush(heap,(-t,t))
print(answ)