import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = sorted(list(int(input()) for _ in range(N)))

start = 0
# time의 최소값 * 사람 수 => 최대 시간 
end = min(time) * M
result = 0

while start <= end :
    mid = (start + end) // 2
    quotient = 0
    for t in time:
        quotient += mid // t

    if quotient >= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
