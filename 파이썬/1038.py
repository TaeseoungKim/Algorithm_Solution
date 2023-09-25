import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
if N >= 1023:
    print(-1)
else:
    downNumbers = []
    for i in range(1, 11):
        combs = list(combinations(range(10), i))
        for comb in combs:
            downNum = "".join(map(str, sorted(comb, reverse=True)))
            downNumbers.append(int(downNum))

    downNumbers.sort()
    print(downNumbers[N])
