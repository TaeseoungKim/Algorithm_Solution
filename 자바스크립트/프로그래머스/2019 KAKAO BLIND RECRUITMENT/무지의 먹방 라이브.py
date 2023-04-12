import heapq

food_times = [3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232,
              4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321, 3, 1, 2, 3062, 3123, 11235, 21, 1123, 254, 1123, 2423, 13421, 1232, 4321]
k = 37345


# 무지의 먹방 라이브


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer


def solution(food_times, k):
    answer = -1
    length = len(food_times)
    board = []

    for i in range(length):
        heapq.heappush(board, (food_times[i], i+1))

    food_num = length
    previous = 0

    while board:
        time = (board[0][0]-previous)*food_num

        if k >= time:
            k -= time
            previous, _ = heapq.heappop(board)
            food_num -= 1
        else:
            idx = k % food_num
            board.sort(key=lambda x: x[1])
            answer = board[idx][1]
            break

    return answer


solution(food_times, k)
