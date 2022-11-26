import datetime


def solution(s, times):

    savingPerDay = 1
    curDate = datetime.datetime.strptime(s, '%Y:%m:%d:%H:%M:%S')
    print("curDate", curDate)

    for Date in times:

        # curDate에서 날짜만 뽑는다
        tempDate = curDate.strftime('%Y:%m:%d')
        tempDate = datetime.datetime.strptime(tempDate, '%Y:%m:%d')

        Date = Date.split(":")
        Day = datetime.timedelta(days=int(Date[0]))
        Hour = datetime.timedelta(hours=int(Date[1]))
        Minute = datetime.timedelta(minutes=int(Date[2]))
        Second = datetime.timedelta(seconds=int(Date[3]))

        nextDay = curDate + Day + Hour + Minute + Second
        newTempDate = nextDay.strftime('%Y:%m:%d')
        newTempDate = datetime.datetime.strptime(newTempDate, '%Y:%m:%d')

        if tempDate == newTempDate:
            curDate = nextDay
            continue
        else:
            curDate = nextDay
            if tempDate+datetime.timedelta(days=1) != newTempDate:
                savingPerDay = 0

    s = datetime.datetime.strptime(s, '%Y:%m:%d:%H:%M:%S')

    tempDate = curDate.strftime('%Y:%m:%d')
    tempDate = datetime.datetime.strptime(tempDate, '%Y:%m:%d')
    newTempDate = s.strftime('%Y:%m:%d')
    newTempDate = datetime.datetime.strptime(newTempDate, '%Y:%m:%d')
    date_diff = tempDate - newTempDate

    return [savingPerDay, date_diff.days+1]
