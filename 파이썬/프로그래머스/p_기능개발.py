
from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    day=0
    result=[]
    while progresses:
        day+=1
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        cnt=0
        while progresses:
            per=progresses.popleft()
            if per>=100:
                cnt+=1
                speeds.popleft()
                if not progresses:
                    result.append(cnt)
                    break    
            else: 
                progresses.appendleft(per)
                if cnt!=0:
                    result.append(cnt)
                break
    return result

progresses=[93, 30, 55]
speeds=[1, 30, 5]
solution(progresses, speeds)