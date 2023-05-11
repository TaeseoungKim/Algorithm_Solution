def timeTominute(time):
    hour, minute = map(int, time.split(":"))
    return hour*60+minute


def solution(x, y, pays):
    pointDict = dict()

    wallet = 0
    point = 0

    added = 0
    deled = 0

    for pay in pays:
        day, time, order = pay.split(" ")
        day = int(day)
        time = timeTominute(time)
        order = int(order)
        tempOrder = int(order)

        for d in range(1, day+1):
            if d in pointDict:
                for p in pointDict[d]:
                    point += p
                pointDict.pop(d)

        # 주문
        if order > 0:
            if order > wallet+point:
                needMoney = order - wallet+point
                quo = needMoney//x
                if needMoney % x != 0:
                    quo = quo+1
                wallet += quo*x
                added += quo*x

            if point > order:
                point -= order
                order = 0
            else:
                order -= point
                point = 0

            wallet -= order

            if day+y in pointDict:
                pointDict[day+y].append(tempOrder*0.1)
            else:
                pointDict[day+y] = list()
                pointDict[day+y].append(tempOrder*0.1)

        else:
            if order == 0:
                continue
            elif abs(order) > wallet:
                deled += wallet
                wallet = 0
            else:
                wallet += order
                deled += abs(order)

    for d in range(1, 30+1):
        if d in pointDict:
            for p in pointDict[d]:
                point += p
            pointDict.pop(d)

    return [added, deled, wallet, point]
