import sys
input = sys.stdin.readline

p1, p2, isWrong = False,0,False #조건 1,2
STR = input().rstrip()
while STR!='end':
    for i in range(len(STR)):
        if not p1 and STR[i] in ['a','e','i','o','u']:
            p1=True
        if p2>=0:
            if STR[i] not in ['a','e','i','o','u']: #p2: 자음 => 자음
                p2+=1
            if STR[i] in ['a','e','i','o','u']: #p2: 자음 => 모음
                p2=-1
        elif p2<=0: #p2: 모음 => 모음
            if STR[i] not in ['a','e','i','o','u']: #p2: 모음 => 자음
                p2=1
            if STR[i] in ['a','e','i','o','u']: #p2: 모음 => 모음
                p2-=1
        if p2==3 or p2==-3:
            isWrong=True
            break
        if i!=0 and STR[i]==STR[i-1]:
            if STR[i] not in ['e','o']:
                isWrong=True
                break
    if isWrong==True or p1==False:
        print(f'<{STR}> is not acceptable.')
    else:
        print(f'<{STR}> is acceptable.')
    STR = input().rstrip()
    p1, p2, isWrong = False,0,False