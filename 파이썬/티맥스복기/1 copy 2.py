
from copy import deepcopy


def backTracking(answer, samePrjKeys, N_assignDict, K_assignDict, cmpLen, samePrj):

    for dev in samePrjKeys:
        if N_assignDict[dev] == 0:
            continue
        for otherDev in samePrj[dev]:
            if N_assignDict[dev] == 0:
                break
            if K_assignDict[otherDev] > 0:
                K_assignDict[otherDev] -= 1
                N_assignDict[dev] -= 1
                answer += otherDev
            else:
                continue

    if len(answer) == cmpLen:
        return answer
    else:
        return False


def solution(prj, n, k):
    samePrj = dict()
    cmpLen = 0
    N_assignDict = dict()
    K_assignDict = dict()

    for developers in prj:
        for i, dev in enumerate(developers):
            for d, otherDev in enumerate(developers):
                if dev == otherDev:
                    continue

                if dev in samePrj:
                    if otherDev in samePrj[dev]:
                        continue
                    else:
                        samePrj[dev].append(otherDev)
                else:
                    samePrj[dev] = []
                    samePrj[dev].append(otherDev)
    for KEY in samePrj.keys():
        samePrj[KEY].sort()
        print(KEY, ":", samePrj[KEY])

    samePrjKeys = []
    for KEY in samePrj.keys():
        samePrjKeys.append(KEY)
    samePrjKeys.sort()

    answer = ""

    for KEY in samePrjKeys:
        N_assignDict[KEY] = n
        K_assignDict[KEY] = k

    cmpLen = len(samePrjKeys)*n
    print("samePrjKeys", samePrjKeys)
    print()
    # 백트래킹이다.

    for dev in samePrjKeys:
        if N_assignDict[dev] == 0:
            continue
        for otherDev in samePrj[dev]:
            if N_assignDict[dev] == 0:
                break

            if K_assignDict[otherDev] > 0:
                K_assignDict[otherDev] -= 1
                N_assignDict[dev] -= 1
                isAnswer = backTracking(answer+otherDev, samePrjKeys, deepcopy(
                    N_assignDict), deepcopy(K_assignDict), cmpLen, samePrj)
                if not isAnswer:
                    K_assignDict[otherDev] += 1
                    N_assignDict[dev] += 1
                    continue
                else:
                    return isAnswer
            else:
                continue

    return answer
