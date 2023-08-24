
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
timeToBuild = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
deq = deque()

for i in range(1,N+1):
   op = list(map(int, input().split()))
   timeToBuild[i] = op[0]
   if len(op) == 2:
      continue
   else:
      for d in range(1,len(op)-1):
        board[op[d]].append(i)
        degree[i] += 1
      
for i in range(1,N+1):
   if degree[i]==0:
      deq.append(i)
      visited[i] = timeToBuild[i]

while deq:
    pNode = deq.popleft()

    for nextNode in board[pNode]:
       degree[nextNode] -= 1
       visited[nextNode] = max(visited[nextNode],visited[pNode]+timeToBuild[nextNode])  

       if degree[nextNode]==0:
          deq.append(nextNode)
          

for i in range(1,N+1):
   print(visited[i])
