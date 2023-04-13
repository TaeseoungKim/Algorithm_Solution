
cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]

pickups = [0, 2, 0, 1, 0, 2, 0]


def solution(cap, n, deliveries, pickups):
    # 둘 중에 제일 먼 곳까지 간다.
    # 그리고 cap 까지 사라진다.
    result = 0
    cnt = 1
    while deliveries or pickups:
        dLen, pLen = len(deliveries), len(pickups)
        dCap, pCap = cap, cap
        dMax, pMax = False, False
        for i in range(dLen-1, -1, -1):
            if dCap == 0:
                break
            if deliveries[i] != 0:
                if dMax == False:
                    dMax = i+1
                if dCap >= deliveries[i]:
                    dCap -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= dCap
                    dCap = 0
            if deliveries[i] == 0:
                deliveries.pop()

        for i in range(pLen-1, -1, -1):
            if pCap == 0:
                break
            if pickups[i] != 0:
                if pMax == False:
                    pMax = i+1
                if pCap >= pickups[i]:
                    pCap -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= pCap
                    pCap = 0
            if pickups[i] == 0:
                pickups.pop()

        result += max(dMax, pMax)*2
    return result


print(solution(cap, n, deliveries, pickups))
