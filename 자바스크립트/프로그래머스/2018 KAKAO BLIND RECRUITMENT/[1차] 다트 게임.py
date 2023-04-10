import re


def solution(dartResult):

    p = re.compile('[0-9][0-9]?[a-zA-Z][#*]?')
    board = p.findall(dartResult)
    boardLen = len(board)

    gradeArr = [0 for i in range(boardLen)]
    for i in range(boardLen):
        result = board[i]
        if result[0].isdigit() and result[1].isdigit():
            result = [board[i][0]+board[i][1], board[i][2]]
            if len(result) == 4:
                result.append(board[i][3])

        basicGrade = int(result[0])
        gradeArr[i] += basicGrade

        if result[1] == "S":
            pass
        elif result[1] == "D":
            gradeArr[i] = gradeArr[i]**2
        elif result[1] == "T":
            gradeArr[i] = gradeArr[i]**3

        if len(result) == 3:
            if result[2] == "*":
                gradeArr[i] = gradeArr[i]*2
                if i != 0:
                    gradeArr[i-1] = gradeArr[i-1]*2
            elif result[2] == "#":
                gradeArr[i] = gradeArr[i]*(-1)

    answer = 0
    for i in range(boardLen):
        answer += gradeArr[i]

    return answer
