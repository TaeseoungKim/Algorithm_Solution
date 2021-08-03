# 항상 문제를 풀 때, 경우의 수 마다 어떤 규칙이 있는지 찾자.
# n = 0 => 1
# n = 1 => 1
# n = 2 => 2
# n = 3 => 3
# n = 4 => 5
# n = 5 => 8


n = int(input())


def fibonach(n):

    if n == 1 or n == 2:
        return n;

    sum = fibonach(n-1) + fibonach(n-2)
    return sum

print(fibonach(n))