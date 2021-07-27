from collections import deque

def bfs(start,end):
    deq = deque()
    deq.append(start)
    visit[start] = 1  
    
    while(deq):
        node = deq.popleft()
        for i in range(1,N+1,1):
            if visit[i] == 0 and nodeList[node][i] == 1:                
                level[i] = level[node] + 1 #체크
                deq.append(i)
                visit[i] = 1
                

N = int(input())
start , end = map(int, input().split())
M = int(input())

nodeList  = [ [0] * (N+1) for i in range(N+1) ] 
level = [ 0 * (N+1) for i in range(N+1) ]

for i in range(M):
     fromNode, toNode = map(int, input().split())
     nodeList[fromNode][toNode] = nodeList[toNode][fromNode] = 1

visit = [ 0 for i in range(N+1) ]

bfs(start,end)

print(level[end] if level[end] != 0 else -1) #체크