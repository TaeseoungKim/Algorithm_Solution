import sys
a, b = map(int, sys.stdin.readline().split())
num = []

i=1
while len(num) < b:
    for _ in range(i):
        num.append(i)
    i += 1
print(sum(num[a-1:b]))