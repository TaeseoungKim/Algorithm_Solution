from collections import deque


def timeToNumber(time):
    splited = time.split(":")
    hour = int(splited[0])
    minute = int(splited[1])
    second = float(splited[2])

    return (hour*3600)+(minute*60)+second


def numberToTime():
    return 3


def roundRobin(numServer, logs):
    assignDis = [deque() for i in range(numServer)]

    count = 0
    for log in logs:
        assignDis[count].append(log)
        count += 1
        if count == numServer:
            count = 0

    maxTime = 0
    for idx, val in enumerate(assignDis):

        curTime = 0
        while assignDis[idx]:
            log = assignDis[idx].popleft()

            reqTime = timeToNumber(log.split(" ")[0])
            prosTime = float(log.split(" ")[1])

            if curTime <= reqTime:
                curTime = reqTime + prosTime
            elif curTime > reqTime:
                curTime += prosTime

        maxTime = max(maxTime, curTime)

    return maxTime


def leastConnection(numServer, logs):
    assignDis = [[False, False] for i in range(numServer)]
    curAssign = [[0, i] for i in range(numServer)]
    logQueue = deque(logs)

    for idx, server in enumerate(assignDis):

        curAssign = sorted(curAssign, key=lambda x: x[0])
        newAssignDis = []

        logQueue.popleft()

        for idxT, valT in enumerate(curAssign):
            newAssignDis.append(assignDis[valT[1]])

        assignDis = sorted(assignDis, )
        assignDis

    return


def solution(numServer, logs):
    rr = roundRobin(numServer, logs)
    rc = leastConnection(numServer, logs)

    print(rr)
