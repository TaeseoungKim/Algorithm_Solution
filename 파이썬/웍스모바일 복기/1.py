from itertools import combinations


def solution(numbers):
    LEN = len(numbers)
    sumV = sum(numbers)
    minV = 2e9

    for i in range(1, LEN//2+1):
        for comb in combinations(numbers, i):
            first = sum(comb)
            second = sumV-first

            sumDiff = abs(first-second)
            minV = min(minV, sumDiff)

    return minV
