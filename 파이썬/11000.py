import sys
input = sys.stdin.readline
N = int(input())
Arr = [list(map(int, input().split(" "))) for i in range(N)]


sortedArr = sorted(Arr, key=lambda x: (x[0], x[1]))
infoDict = dict()
curV = 0
maxV = 0
for I, V in enumerate(sortedArr):
    print(V, "curV", curV,)
    infoDict.setdefault(V[0], 0)
    curV -= infoDict[V[0]]
    infoDict[V[0]] = 0

    infoDict.setdefault(V[1], 0)
    infoDict[V[1]] += 1
    curV += 1
    maxV = max(maxV, curV)

print("infoDict", infoDict)
print(maxV)
