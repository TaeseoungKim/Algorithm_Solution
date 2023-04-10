# 3시 시작
from collections import deque

# 딕셔너리와 데크를 이용한다.
cacheSize = 3
cities = ["a", "b", "c", "a", "b", "d", "c"]


def solution(cacheSize, cities):
    cache = deque()
    cacheDict = dict()
    executeTime = 0

    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        CITY = city.upper()
        if CITY not in cacheDict.keys():
            cacheDict[CITY] = False

    for city in cities:
        CITY = city.upper()
        if cacheDict[CITY]:
            while True:
                popItem = cache.popleft()
                cache.append(popItem)

                if popItem == CITY:
                    break
            executeTime += 1
        elif len(cache) < cacheSize:
            cache.append(CITY)
            cacheDict[CITY] = True
            executeTime += 5
        else:
            popItem = cache.popleft()
            cacheDict[popItem] = False
            cacheDict[CITY] = True
            cache.append(CITY)
            executeTime += 5
    return executeTime


print(solution(cacheSize, cities))
