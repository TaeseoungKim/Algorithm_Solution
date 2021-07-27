from collections import deque


def dfs(V):
    visit[V] = 1
    print(V,end=" ")
    for i in range(1,N+1,1):
        if visit[i] == 0 and nodeList[V][i] == 1:
            dfs(i)

def bfs(V):
    deq = deque()
    deq.append(V)
    visit[V] = 1  
    print(V,end=" ")
    
    while(deq):
        node = deq.popleft()
        for i in range(1,N+1,1):
            if visit[i] == 0 and nodeList[node][i] == 1:
                deq.append(i)
                visit[i] = 1
                print(i,end=" ")
                



N , M , V = map(int, input().split())

nodeList  = [ [0] * (N+1) for i in range(N+1) ] 

for i in range(M):
     fromNode, toNode = map(int, input().split())
     nodeList[fromNode][toNode] = nodeList[toNode][fromNode] = 1

visit = [ 0 for i in range(N+1) ]
dfs(V)
print()
visit = [ 0 for i in range(N+1) ]
bfs(V)
