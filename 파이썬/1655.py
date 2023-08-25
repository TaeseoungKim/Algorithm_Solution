import sys
import heapq
input = sys.stdin.readline

N = int(input())
maxHeap, minHeap = [], []

answer = []
for i in range(N):
    num = int(input())
    if len(maxHeap) == len(minHeap):
        heapq.heappush(maxHeap, -num)
    else: 
        heapq.heappush(minHeap, num)

    if minHeap and  minHeap[0] < -maxHeap[0] :
        maxValue = heapq.heappop(maxHeap)
        minValue = heapq.heappop(minHeap)

        heapq.heappush(minHeap,-maxValue)
        heapq.heappush(maxHeap,-minValue)
    
    print(-maxHeap[0])