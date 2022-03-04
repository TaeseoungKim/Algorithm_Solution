def solution(n, times):
    left=1
    right=max(times)*n
    mid = (left+right)//2
    answer=0
    while left<=right:
        people=0
        mid=(left+right)//2
        for time in times:
            people+= mid//time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break
        if people>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1

    print(answer)
    return answer
n=6	
times=[7, 10]
solution(n,times)