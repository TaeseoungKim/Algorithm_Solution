import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

def dfs(v):
    arr[v]=-2
    for i in range(n):
        if v==arr[i]:
            dfs(i)
            
dfs(k)
result = 0
for i in range(n):
    if arr[i]!=-2 and i not in arr:
        result += 1
print(result)