import sys
input = sys.stdin.readline

while True:
    board = input().strip()
    if not board:
        break

    sub, sequence = board.split()

    alphaDict = dict()
    for c in sub:
        alphaDict[c] = True

    tempSequence = ""
    for c in sequence:
        if c not in alphaDict.keys():
            continue
        tempSequence += c

    curIdx = 0
    isYes = True
    for c1 in sub:
        isPossible = False

        for i in range(curIdx, len(tempSequence)):

            if c1 == tempSequence[i]:
                isPossible = True
                curIdx += 1
                break
            curIdx += 1
        if not isPossible:
            isYes = False
            break

    if isYes:
        print("Yes")
    else:
        print("No")
