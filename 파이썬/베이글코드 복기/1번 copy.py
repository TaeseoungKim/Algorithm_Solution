from collections import deque


def solution(n, edges):

    nodeDict = dict()

    for n1, n2 in edges:
        if n1 in nodeDict:
            nodeDict[n1].add(n2)
        else:
            nodeDict[n1] = set()
            nodeDict[n1].add(n2)

    minInfected = 51

    def bfs(nextNodes, infected):
        nonlocal minInfected

        newSet = set()
        for nextNode in nextNodes:
            if nextNode in nodeDict:
                for node in nodeDict[nextNode]:
                    newSet.add(node)

        # 새로 감염시킬 얘들이 없으면
        if not newSet:
            minInfected = min(minInfected, infected)
            return

        newDeque = deque(list(newSet))
        newInfected = len(newDeque)-1

        for i in range(len(newDeque)):
            tempNode = newDeque.popleft()
            bfs(set(newDeque), infected+newInfected)
            newDeque.append(tempNode)

    bfs(set([0]), 1)
    return minInfected
