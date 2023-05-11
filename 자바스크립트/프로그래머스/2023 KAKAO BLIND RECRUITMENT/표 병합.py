commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2",
            "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]


def MERGE(op, board):
    r1, c1, r2, c2 = int(op[1]), int(
        op[2]), int(op[3]), int(op[4])
    if r1 == r2 and c1 == c2:
        return

    unionSet = set()
    unionSet.add((r1, c1))
    unionSet.add((r2, c2))
    unionSet = unionSet.union(board[r1][c1][1].union(board[r2][c2][1]))

    board[r1][c1][1] = unionSet
    board[r2][c2][1] = unionSet

    for tr, tc in unionSet:
        if (tr == r1 and tc == c1) or (tr == r2 and tc == c2):
            continue
        board[tr][tc][1] = board[tr][tc][1].union(unionSet)

    board[r1][c1][2] = True
    board[r2][c2][2] = True

    if board[r1][c1][0] != "" and board[r2][c2][0] == "":
        for r, c in unionSet:
            board[r][c][0] = board[r1][c1][0]

    if board[r1][c1][0] == "" and board[r2][c2][0] != "":
        for r, c in unionSet:
            board[r][c][0] = board[r2][c2][0]

    if board[r1][c1][0] != "" and board[r2][c2][0] != "":
        for r, c in unionSet:
            board[r][c][0] = board[r1][c1][0]


def UNMERGE(op, board):
    r, c = int(op[1]), int(op[2])
    value = board[r][c][0]
    mergedSet = board[r][c][1]

    if board[r][c][2] == False:
        return

    for tr, tc in mergedSet:
        board[tr][tc] = ["", set(), False]
    board[r][c] = [value, set(), False]


def UPDATE(op, board):
    if len(op) == 4:
        r, c, value = int(op[1]), int(op[2]), op[3]
        if board[r][c][2]:
            mergedSet = board[r][c][1]
            mergedSet.add((r, c))
            for tr, tc in mergedSet:
                board[tr][tc][0] = value
        else:
            board[r][c][0] = value

    if len(op) == 3:
        _, value1, value2 = op
        for r in range(1, 51):
            for c in range(1, 51):
                if board[r][c] == value1:
                    if board[r][c][2]:
                        mergedSet = board[r][c][1]
                        mergedSet.add((r, c))
                        for tr, tc in mergedSet:
                            board[tr][tc][0] = value2
                    else:
                        board[r][c][0] = value2


def solution(commands):
    board = [[["", set(), False] for _ in range(51)] for _ in range(51)]
    result = []
    for command in commands:
        op = command.split()

        if op[0] == "UPDATE":
            UPDATE(op, board)
        elif op[0] == "MERGE":
            MERGE(op, board)
        elif op[0] == "UNMERGE":
            UNMERGE(op, board)
        elif op[0] == "PRINT":
            r, c = int(op[1]), int(op[2])
            if board[r][c][0] == "":
                result.append("EMPTY")
            else:
                result.append(board[r][c][0])

    return result


print(solution(commands))
