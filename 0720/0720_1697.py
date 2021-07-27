from collections import deque

MAX = 10**5
start_x, end_x = map(int, input().split()) 
visit = [0 for _ in range(MAX+1)] 

deq = deque()    
deq.append(start_x)    

while deq.__len__() != 0:
    pop_x = deq.popleft()
    
    if pop_x == end_x :
        print(visit[end_x])
        break

    for tmp_x in (pop_x-1, pop_x+1, pop_x*2):  # 체크
        if (0 <= tmp_x <= MAX) != True:
            continue
        elif visit[tmp_x] == 0:
            deq.append(tmp_x)
            visit[tmp_x] = visit[pop_x] + 1

exit(0)