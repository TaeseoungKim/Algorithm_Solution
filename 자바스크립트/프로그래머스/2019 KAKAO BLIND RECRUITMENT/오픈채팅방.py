records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
           "Enter uid1234 Prodo", "Change uid4567 Ryan"]

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(records):
    userDict = dict()  # [Key:UID] NickName, isEnter
    result = []

    for record in records:
        op = record.split(" ")
        if op[0] == "Enter":
            if op[1] in userDict:
                userDict[op[1]][0] = op[2]
                userDict[op[1]][1] = True
            elif op[1] not in userDict:
                userDict[op[1]] = [op[2], True]
        elif op[0] == "Leave":
            userDict[op[1]][1] = False
        elif op[0] == "Change":
            userDict[op[1]][0] = op[2]

    for record in records:
        op = record.split(" ")
        if op[0] == "Enter":
            result.append(userDict[op[1]][0]+"님이 들어왔습니다.")
        elif op[0] == "Leave":
            result.append(userDict[op[1]][0]+"님이 나갔습니다.")

    return result


solution(records)
