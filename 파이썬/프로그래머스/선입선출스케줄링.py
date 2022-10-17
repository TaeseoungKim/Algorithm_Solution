n = 6
cores = [1, 2, 3]


def solution(n, cores):

    # 시간을 기준으로 이분탐색 진행
    left = 1
    right = max(cores)*n

    if n <= len(cores):
        return n

    while left < right:
        mid = (left+right)//2
        capa = 0

        for core in cores:
            capa += mid//core

        if capa >= n:
            right = mid
        else:
            left = mid+1

    print("right", right)

    n -= sum(map(lambda x: (right-1)//x, cores))
    print("n", n)

    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i+1


print(solution(n, cores))
