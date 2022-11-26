def solution(id_list, k):
    customer = dict()
    for order in id_list:
        newSet = set(order.split(" "))
        for ID in newSet:
            if ID in customer:
                if customer[ID] < k:
                    customer[ID] += 1
            else:
                customer[ID] = 1

    answer = 0
    for KEY in customer.keys():
        answer += customer[KEY]
    return answer
