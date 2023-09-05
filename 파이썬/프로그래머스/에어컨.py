import sys
sys.setrecursionlimit(1000000)


def solution(temperature, t1, t2, a, b, onboard):
    finalTime = len(onboard)-1
    

    def recursion(time, curTemp, curElectric):
        if onboard[time]==1 and not (t1 <= curTemp <= t2):
            return sys.maxsize
        
        if finalTime==time:
            return curElectric

        minElectric = sys.maxsize
        if curTemp > temperature:
            minElectric = min(minElectric, recursion(time+1, curTemp-1, curElectric))  
        elif curTemp < temperature:
            minElectric = min(minElectric, recursion(time+1, curTemp+1, curElectric))  
        else:
            minElectric = min(minElectric, recursion(time+1, curTemp, curElectric)) 

        minElectric = min(minElectric, recursion(time+1, curTemp+1, curElectric+a))
        minElectric = min(minElectric, recursion(time+1, curTemp-1, curElectric+a))
        minElectric = min(minElectric, recursion(time+1, curTemp, curElectric+b))

        return minElectric
    
    answer = sys.maxsize
    answer = min(answer, recursion(1, temperature, 0)) 
    answer = min(answer, recursion(1, temperature+1, a))
    answer = min(answer, recursion(1, temperature-1, a))
    return answer