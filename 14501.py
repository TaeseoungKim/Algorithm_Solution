import sys
input = sys.stdin.readline

N = int(input())
T, P, result = [], [], [0 for _ in range(N)]
for _ in range(N):
    day, value = map(int, input().split())
    T.append(day)
    P.append(value)
print(P)

for i in range(N):
    if T[i] + i > N:
        continue
    else:
        result[T[i]+i] = max(result[i]+P[T[i]+i], result[T[i]+i]) 

print(result)
print(max(result))