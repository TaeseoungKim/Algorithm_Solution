from collections import deque

n = 10
t = 60
m = 45

timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
             "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]


def minutesToTime(num):
    hour = str(num//60)
    minute = str(num % 60)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    return hour + ":" + minute


def timeToMinutes(str):
    hour, minute = str.split(":")
    Minutes = int(hour)*60 + int(minute)
    return Minutes


def solution(n, t, m, timetable):
    board = []
    result = 0

    for time in timetable:
        board.append(timeToMinutes(time))

    board = sorted(board)
    board = deque(board)

    for i in range(n):
        capa = m
        busTime = 540+(i*t)

        while board:
            personTime = board.popleft()

            if personTime > busTime or capa == 0:
                board.appendleft(personTime)
                break
            else:
                capa -= 1
            if not board:
                result = minutesToTime(personTime-1)
                break
        if result != 0:
            break
        elif not board:
            result = minutesToTime(busTime)
            break

    return result


solution(n, t, m, timetable)
