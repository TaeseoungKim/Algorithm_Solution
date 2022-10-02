


def solution(n, l, r):
    result=0
    lost=[0]*(n+1)
    reserve=[0]*(n+1)

    for i in range(n+1):
        if i in l and i in r:
            continue
        elif i in l:
            lost[i]=1
        elif i in r:
            reserve[i]=1

    for i in range(1,n+1):
        if lost[i]==1:
            if 1<=i-1 and reserve[i-1]==1:
                reserve[i-1]=0
                result+=1
                continue
            elif i+1<=n and reserve[i+1]==1:
                reserve[i+1]=0
                result+=1
                continue
            else: 
                continue
        result+=1
    return result

n=5
lost=[2,4]	
reserve=[3,5]
solution(n, lost, reserve)
reserve_dic = dict()