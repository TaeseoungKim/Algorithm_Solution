from itertools import combinations

relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]


def solution(relation):
    wid = len(relation[0])
    hei = len(relation)
    board = [[] for i in range(wid)]

    for i in range(wid):
        for d in range(hei):
            board[i].append(relation[d][i])

    for i in range(wid):
        print(board[i])

    for i in range(wid):
        comb = combinations(board, i+1)
        print(list(comb))

    answer = 0
    return answer


solution(relation)
