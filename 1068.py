import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
ntree = [[]for _ in range(n)]
edges = list(map(int,input().split()))
removed = [0]*n
remove_node = int(input())
root_node = -1
for i in range(n):
    if edges[i]!=-1:
        ntree[edges[i]].append(i)
    else: root_node=i

cnt = 0
def remove_dfs(rn):
    global cnt
    if cnt == 10:
        return
    else: cnt += 1
    removed[rn]=1
    if len(ntree[rn])!=0:
        for n in ntree[rn]:
            remove_dfs(n)

result = 0
def dfs(n):
    child = 0
    if len(ntree[n])!=0:
        for i in ntree[n]:
            if removed[i]!=1:
                child += 1
                dfs(i)
    if child==0:
        global result
        result+=1
    

remove_dfs(remove_node)
dfs(0)
if remove_node==root_node:
    print(0)
else:
    print(result)