import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    while scoville:
        tmp1=heapq.heappop(scoville)
        if tmp1>=K:
            break
        else:
            if scoville:
                tmp2=heapq.heappop(scoville)
            else: return -1
            cnt+=1
            heapq.heappush(scoville,tmp1+tmp2*2)
    return cnt


scoville=[1, 10, 12, 2, 3, 9]
K=7
print(solution(scoville, K))
