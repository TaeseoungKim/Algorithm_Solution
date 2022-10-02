from collections import deque
import sys

def dfs(v,wei):
    max_v,i=wei,v
    deq = deque()
    deq.append((v,wei))
    while deq:
        pop_v, pop_wei = deq.pop()
        visit[pop_v]=1
        for tmp_v,tmp_wei in board[pop_v]:
            if visit[tmp_v]==0:
                deq.append((tmp_v,pop_wei+tmp_wei))
                if pop_wei+tmp_wei > max_v:
                    max_v, i = pop_wei+tmp_wei, tmp_v
    return max_v,i
input = sys.stdin.readline
n = int(input())
board = [[] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for d in range(1,len(tmp)-2,2):
        board[tmp[0]].append([tmp[d],tmp[d+1]])

visit = [0]*(n+1)
max_v, i = dfs(1,0)
visit = [0]*(n+1)
max_v, i = dfs(i,0)
print(max_v)
