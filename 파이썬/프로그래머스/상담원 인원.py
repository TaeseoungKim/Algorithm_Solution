from copy import deepcopy
import heapq
import sys


k = 1
n = 1
reqs = [[5, 55, 1], [10, 90, 1], [10, 40, 1], [50, 45, 1], [100, 50, 1]]

def initAllCase(allCase, curCase, kIndex, maxK, nIndex, maxN):
    tempCurCase = deepcopy(curCase)
    tempCurCase[kIndex] += 1
    
    if nIndex == maxN:
        allCase.append(tempCurCase)
        return

    for i in range(kIndex, maxK):
        initAllCase(allCase, tempCurCase, i, maxK, nIndex+1, maxN)

def getWaitTime(mentoCase, reqs):
    mentoQueue = [[] for i in range(len(mentoCase))]
    waitTime = 0

    for req in reqs:
        start, time, case = req
        if len(mentoQueue[case-1]) < mentoCase[case-1]:
            heapq.heappush(mentoQueue[case-1], start+time)
        else:
            endTime = heapq.heappop(mentoQueue[case-1]) 
            if endTime > start:
                waitTime += endTime - start
                heapq.heappush(mentoQueue[case-1], endTime+time)
            else:
                heapq.heappush(mentoQueue[case-1], start+time)
    return waitTime

def solution(k, n, reqs):
    allCase = []

    if n-k == 0:
        allCase.append([1 for _ in range(k)])
    else:
        for i in range(k):
            initAllCase(allCase, [1 for _ in range(k)], i, k, 1, n-k)
    
    minWait = sys.maxsize

    for i in range(len(allCase)):
        minWait = min(minWait, getWaitTime(allCase[i], reqs)) 
    
    return minWait

solution(k, n, reqs)