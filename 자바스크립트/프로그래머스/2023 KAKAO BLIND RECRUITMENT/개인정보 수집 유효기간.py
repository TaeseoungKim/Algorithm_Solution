today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


def calDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 28 * 12) + month * 28 + day


def solution(today, terms, privacies):
    today = calDay(today)
    result = []

    termDic = dict()
    for term in terms:
        alpha, month = term.split()
        termDic[alpha] = int(month)

    board = []
    for privacy in privacies:
        date, term = privacy.split(" ")
        date = calDay(date)
        date += termDic[term]*28-1
        board.append(date)
    for idx, date in enumerate(board):
        if board[idx] < today:
            result.append(idx+1)
    return result


print(solution(today, terms, privacies))
