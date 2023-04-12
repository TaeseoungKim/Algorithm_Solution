from collections import deque

food_times = [3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232,
              4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321]
k = 37345


def solution(food_times, k):
    food_kinds = len(food_times)
    deq = deque()

    for i in range(food_kinds):
        deq.append((i+1, food_times[i]))

    while (True):
        idx, value = deq.popleft()

        if k == 0:
            return idx

        value -= 1
        k -= 1

        if value != 0:
            deq.appendleft((idx, value))
            deq.rotate(-1)

        if len(deq) == 0:
            return -1


print(solution(food_times, k))
