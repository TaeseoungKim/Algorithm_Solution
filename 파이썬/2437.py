import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int,input().split()))
weights.sort()

target = 1

for weight in weights:
  if target < weight:
    break
  else:
    target += weight

print(target)