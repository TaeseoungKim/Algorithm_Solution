

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    board1 = [[" " for _ in range(n)] for _ in range(n)]
    board2 = [[" " for _ in range(n)] for _ in range(n)]

    for i in range(n):
        binary = 2**(n-i-1)
        for d in range(n):
            number1 = arr1[d]//binary
            number2 = arr2[d]//binary

            if number1 == 1:
                arr1[d] -= binary
                board1[d][i] = "#"
            if number2 == 1:
                arr2[d] -= binary
                board2[d][i] = "#"

    result = ["" for _ in range(n)]
    for i in range(n):
        for d in range(n):
            if board1[i][d] == "#" or board2[i][d] == "#":
                result[i] += "#"

            if board1[i][d] == " " and board2[i][d] == " ":
                result[i] += " "

    return result


solution(n, arr1, arr2)
