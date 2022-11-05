import sys
input = sys.stdin.readline

N, Wallet = map(int, input().split(" "))
board = list(map(int, input().split(" ")))
newDict = dict()

for i, v in enumerate(board):
    if v in newDict:
        newDict[v] = newDict[v]+1
    else:
        newDict[v] = 1

left = 1
right = 10**9
mid = (left+right)//2
minCapa = (left+right)//2

while left <= right:

    mid = (left+right)//2
    newValue = 0

    for v, num in newDict.items():
        if v < mid:
            newValue += ((mid-v)**2)*num

    if Wallet < newValue:
        right = mid-1
    elif Wallet >= newValue:
        minCapa = mid
        left = mid+1

print(minCapa)
