def solution(flowers):
    calendar = [0 for i in range(366)]
    flowerDay = [1 for i in range(366)]
    for start, end in flowers:
        calendar[start:end] = flowerDay[start:end]
    return sum(calendar)
