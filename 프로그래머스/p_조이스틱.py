

def solution(t):
    name = []
    for c in t:
        name.append(ord(c)-65)
    
    result=0
    
    for n in name:
        cursor=0
        isNegative=0
        if n==cursor==0: continue
        if n-cursor>0: isNegative=False
        else: isNegative=True
        case1 = abs(n-cursor)
        case2 = 1+n #왼쪽으로 쭉 이동 후, 찾아감
        case3 = 1+(25-n)#오른쪽으로 쭉 이동 후, 찾아감
        result += min(case1,case2,case3)

    print(result)


solution("JEROEN")