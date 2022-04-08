import sys
input = sys.stdin.readline

n, s = map(int, input().split())
board = list(map(int, input().split()))
ans = [0]*n
print(board)

for i in range(n):
    for d in range(n):
        for k in range(d,i+1):
        ans[i]