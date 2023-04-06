T = [
    ["FRANCE", "french"],
    ["handshake", "shake hands	"],
    ["aa1+aa2", "AAAA12"],
    ["E=M*C^2", "e=m*c^2"],
]


def solution(str1, str2):
    left = []
    for i in range(0, len(str1)):
        word = str1[i]+str1[i+1]
        if word.isalpha():
            left.append(word.upper())
        if i+1 == len(str1)-1:
            break

    right = []
    for i in range(0, len(str2)):
        word = str2[i]+str2[i+1]
        if word.isalpha():
            right.append(word.upper())
        if i+1 == len(str2)-1:
            break

    unionSet = set(left).union(set(right))
    intersectV = 0
    unionV = 0

    for key in unionSet:
        leftCnt = left.count(key)
        rightCnt = right.count(key)
        intersectV += min(leftCnt, rightCnt)
        unionV += max(leftCnt, rightCnt)

    if intersectV == 0 and unionV == 0:
        result = 1
    elif intersectV != 0 and unionV == 0:
        result = 1
    else:
        result = intersectV/unionV
    return int(result*65536)


for str1, str2 in T:
    solution(str1, str2)
