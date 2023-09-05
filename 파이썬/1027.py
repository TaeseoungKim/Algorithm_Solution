import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))
maxHeight = max(board)

maxBuildings = []

for i in range(N):
    if maxHeight == board[i]:
        maxBuildings.append(i)

answer = 0

def isUnder(maxBuilding, targetBuilding, curBuilding, lineValue, lineIndex):
    quantity = (maxBuilding - targetBuilding) / lineValue
    quantity*lineIndex

    return True

for maxBuilding in maxBuildings:
    tempAnswer = 0

    for i in range(maxBuilding-1, -1, -1):
        if i == maxBuilding-1:
            tempAnswer += 1
            continue
        
        for d in range(maxBuilding-1, i, -1):
            isUnder(board[maxBuilding], board[i], board[d], maxBuilding-i)
            break
        else:
            break
        
        
    
    answer = max(answer, tempAnswer)

print(answer)
    
