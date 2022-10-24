def solution(n, entry):

    # 입장할 방을 구하는 함수. 게임 방의 수는 무한대다
    def findRoom(board):
        Length = len(board)

        if sum(board) == n*(Length-1):  # 다 찼을 경우
            return False
        maxV, roomNum = -1, -1
        for i in range(1, Length):
            if board[i] == n:
                continue
            if maxV < board[i]:
                maxV = board[i]
                roomNum = i

        return roomNum

    board = [0]
    ans = []
    for i, v in enumerate(entry):
        if v == 0:
            roomNum = findRoom(board)
            if roomNum == False:
                board.append(0)
                roomNum = len(board)-1
            board[roomNum] += 1
            ans.append(roomNum)
        else:
            board[v] -= 1

    return ans
