import sys
alp = 10
cop = 10
problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]


def dfs(alp, cop, problems,  time, minTime, finalAlp, finalCop):
    if alp >= finalAlp and cop >= finalCop:
        return min(minTime, time)

    isImposs = True
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        if alp >= alp_req and cop >= cop_req:
            isImposs = False
            minTime = dfs(alp+alp_rwd, cop+cop_rwd, problems,
                          time+cost, minTime, finalAlp, finalCop)
    if isImposs:
        minAlp, minCop = sys.maxsize, sys.maxsize
        for problem in problems:
            alp_req, cop_req, _, _, _ = problem
            minAlp = min(minAlp, alp_req)
            minCop = min(minCop, cop_req)
        for i in range(minAlp-alp):
            time += 1
            alp += 1
        for i in range(minCop-cop):
            time += 1
            cop += 1

    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        if alp >= alp_req and cop >= cop_req:
            minTime = dfs(alp+alp_rwd, cop+cop_rwd, problems,
                          time+cost, minTime, finalAlp, finalCop)
    return minTime


def solution(alp, cop, problems):
    minTime = sys.maxsize
    finalAlp, finalCop = 0, 0
    for idx, problem in enumerate(problems):
        alp_req, cop_req, _, _, _ = problem
        finalAlp = max(finalAlp, alp_req)
        finalCop = max(finalCop, cop_req)

    minTime = dfs(alp, cop, problems,
                  0, minTime, finalAlp, finalCop)
    return minTime


print(solution(alp, cop, problems))
