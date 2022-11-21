
def solution(infos, actions):
    userInfos = dict()
    isLogin = False
    answer = []
    basket = False

    for info in infos:
        ID, PW = info.split(" ")
        userInfos[ID] = PW

    for action in actions:
        OP = action.split(" ")
        OPCODE = len(OP)
        if OPCODE == 3:
            if isLogin:
                answer.append(False)
            else:
                if OP[1] in userInfos:
                    if userInfos[OP[1]] == OP[2]:
                        isLogin = True
                        answer.append(True)
                    else:
                        answer.append(False)
                else:
                    answer.append(False)
        elif OPCODE == 2:
            if isLogin:
                basket = True
                answer.append(True)
            else:
                answer.append(False)
        elif OPCODE == 1:
            if basket:
                answer.append(True)
                basket = False
            else:
                answer.append(False)
    return answer