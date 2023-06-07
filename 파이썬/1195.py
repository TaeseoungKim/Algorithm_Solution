firstGear = input().strip()
secondGear = input().strip()

if len(firstGear) > len(secondGear):
    smallGear = secondGear
    bigGear = firstGear
elif len(firstGear) < len(secondGear):
    smallGear = firstGear
    bigGear = secondGear
else:
    smallGear = firstGear
    bigGear = secondGear

bigGear = len(smallGear)*"0" + bigGear + len(smallGear)*"0"

bigLen = len(bigGear)
smallLen = len(smallGear)

result = [len(bigGear)]
for i in range(len(bigGear)):
    board = [False for i in range(bigLen)]
    isTrue = True
    smallIdx = 0
    for d in range(i, i+smallLen):
        if int(bigGear[d]) == 2 and int(bigGear[d]) == int(smallGear[smallIdx]):
            isTrue = False
            break
        if bigGear[d] == 0 or (int(bigGear[d]) + int(smallGear[smallIdx]) == 3):
            board[d] = True
            smallIdx += 1

    if isTrue:
        result.append(board.count(True))
print(min(result))
