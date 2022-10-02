import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list( map(int, input().split())))
B = list( map(int, input().split()))
result = 0

for _ in range(N):
    max_idx = B.index(max(B))
    result += A[_]*B.pop(max_idx)
print(result)