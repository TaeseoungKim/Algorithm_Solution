triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

N = len(triangle)
for i in range(1, N):
    M = len(triangle[i])
    for d in range(M):
        if d == 0:
            triangle[i][d] += triangle[i-1][d]
        elif d == M-1:
            triangle[i][d] += triangle[i-1][d-1]
        else:
            triangle[i][d] += max(triangle[i-1][d-1], triangle[i-1][d])


answer = max(triangle[N-1])

for i in range(N):
    print(triangle[i])
print(max(triangle[N-1]))
