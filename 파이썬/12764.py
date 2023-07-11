import sys
import heapq

input = sys.stdin.readline
N = int(input())
board = dict()
heapArr = []
EmptyHeap = []

for i in range(N):
    start, end = map(int, input().split())
    board[start] = ("START", end)
    board[end] = ("END", 0)
    heapq.heappush(heapArr,start)
    heapq.heappush(heapArr,end)

maxComputer = 0
curNumber = 0
pcUsingCnt = dict()

while heapArr:
    key = heapq.heappop(heapArr)
    if board[key][0]=="START":
        curNumber += 1
        maxComputer = max(maxComputer, curNumber)
        _, end = board[key] 
        
        if EmptyHeap:
            pcNum = heapq.heappop(EmptyHeap)
            pcUsingCnt[pcNum] = pcUsingCnt[pcNum]+1
            board[end] = ("END", pcNum)
        
        elif not EmptyHeap:
            pcUsingCnt[curNumber] = 1 
            board[end] = ("END",curNumber)

            
    elif board[key][0]=="END":
        curNumber -= 1
        _, pcNum = board[key]
        heapq.heappush(EmptyHeap,pcNum)



print(maxComputer)
for key in pcUsingCnt.keys():
    print(pcUsingCnt[key],end=" ")