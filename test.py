import sys
from collections import deque

def solution(food_times, k):
    food_kinds=len(food_times)
    deq = deque()
    
    for i in range(food_kinds):
        deq.append((i+1,food_times[i]))    
    print("init: ", deq)
    
    while(True):
        print(deq)
        idx, value = deq.popleft()
        
        print('idx: ',idx,'value: ', value)
        if k==0:
            return idx
        
        value -= 1
        k -= 1
        
        print('idx: ',idx,'value: ', value)
        if value != 0:
            deq.appendleft((idx, value))
            deq.rotate(-1)            
        
        if len(deq)==0:
            return -1



t = [4,2,3,6,7,1,5,8]
print(solution(t,16))