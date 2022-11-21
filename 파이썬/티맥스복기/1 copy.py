
# 상하의
def solution(color, prices):
    sameColor = 0
    diffColor = 0
    topColorInfos = dict()
    bottomColorInfos = dict()
    colorDict = dict()

    for col in color:
        for i in range(0, 2):
            colorDict[col[i]] = 1
            if col[i] not in topColorInfos:
                topColorInfos[col[i]] = 0
            if col[i] not in bottomColorInfos:
                bottomColorInfos[col[i]] = 0

            if i == 0:
                topColorInfos[col[i]] += 1
            if i == 1:
                bottomColorInfos[col[i]] += 1

    print("before")
    print("topColorInfos", topColorInfos)
    print("bottomColorInfos", bottomColorInfos)
    print("same", sameColor)
    print("diff", diffColor)
    print()

    for col in colorDict.keys():
        if topColorInfos[col] > bottomColorInfos[col]:
            topColorInfos[col] -= bottomColorInfos[col]
            sameColor += bottomColorInfos[col]
            bottomColorInfos[col] = 0
        elif topColorInfos[col] < bottomColorInfos[col]:
            bottomColorInfos[col] -= topColorInfos[col]
            sameColor += topColorInfos[col]
            topColorInfos[col] = 0
        else:
            sameColor += topColorInfos[col]
            topColorInfos[col] = 0
            bottomColorInfos[col] = 0

    print(colorDict.keys())
    for col in colorDict.keys():
        if topColorInfos[col] > 0:
            diffColor += topColorInfos[col]
        if bottomColorInfos[col] > 0:
            diffColor += bottomColorInfos[col]

    print("after")
    print("topColorInfos", topColorInfos)
    print("bottomColorInfos", bottomColorInfos)
    print("same", sameColor)
    print("diff", diffColor)

    if prices[0]*2 < prices[1]:
        answer = sameColor*prices[0] + diffColor*prices[0]
    else:
        answer = sameColor*prices[0] + (diffColor//2)*prices[1]
    return answer
