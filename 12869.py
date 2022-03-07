from collections import deque
import heapq
n=int(input())
scv_hp = list(map(int,input().split()))
heapq.heapify(scv_hp)
deq = deque()
damage = [9,1,3]

result=0
while n!=0:
    tmp = 0
    result+=1
    print(scv_hp,result)
    for i in range(n-1,-1,-1):
        tmp = heapq.heappop(scv_hp)-damage[i]
        if tmp>0:
            deq.append(tmp)
        else: n-=1

    while deq: heapq.heappush(scv_hp,deq.pop())

print(result)
