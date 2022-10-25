def checkBingo(board):
    CNT = 0
    for i in range(3):
        if sum(board[i]) == 3:  # 가로
            CNT += 1
        if board[0][i]+board[1][i]+board[2][i] == 3:  # 가로
            CNT += 1

    if board[0][0]+board[1][1]+board[2][2] == 3:
        CNT += 1
    if board[0][2]+board[1][1]+board[2][0] == 3:
        CNT += 1

    return CNT


def solution(logs):

    Dbingo = [[0, 0, 0] for _ in range(3)]
    Wbingo = [[0, 0, 0] for _ in range(3)]
    Mbingo = [[0, 0, 0] for _ in range(3)]
    answ = 0

    for i, log in enumerate(logs):
        if i != 0:
            if logs[i][0] != logs[i-1][0]:  # 날이 달라진다면
                answ += checkBingo(Dbingo)
                Dbingo = [[0, 0, 0] for _ in range(3)]

            if (logs[i][0]-1)//7 != (logs[i-1][0]-1)//7:  # 주가 바뀐다면
                answ += checkBingo(Wbingo)
                Wbingo = [[0, 0, 0] for _ in range(3)]

        if 1 <= logs[i][1] <= 9:  # 일간빙고 수행
            row = (logs[i][1]-1)//3
            col = (logs[i][1]-1) % 3
            Dbingo[row][col] = 1

        elif 10 <= logs[i][1] <= 18:  # 주간빙고 수행
            row = (logs[i][1]-1)//3-3
            col = (logs[i][1]-1) % 3
            Wbingo[row][col] = 1

        elif 19 <= logs[i][1] <= 27:  # 월간빙고 수행
            row = (logs[i][1]-1)//3-6
            col = (logs[i][1]-1) % 3
            Mbingo[row][col] = 1

        if len(logs)-1 == i:
            # 마지막로그
            # 마지막로그
            answ += checkBingo(Dbingo)+checkBingo(Wbingo)+checkBingo(Mbingo)

    return answ
