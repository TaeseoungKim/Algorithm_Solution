import sys
input = sys.stdin.readline

TestCase = int(input())
for _ in range(TestCase):
    F = int(input())
    networkIdx = 0
    friendNetwork = dict()

    for f in range(F):
        
        friendA, friendB = input().strip().split()
        keyList = list(friendNetwork.keys())
        friendA_KEY = -1
        friendB_KEY = -1

        for key in keyList:
            if friendA in friendNetwork[key]["friends"]:
                friendA_KEY = key
            if friendB in friendNetwork[key]["friends"]:
                friendB_KEY = key


        # 둘 다 네트워크에 속해있지 않을 때
        if friendA_KEY == -1 and friendB_KEY == -1:
            friendNetwork[networkIdx] = dict()
            friendNetwork[networkIdx]["friends"] = [friendA,friendB]
            friendNetwork[networkIdx]["count"] = 2
            networkIdx += 1
            print(2)

        # 한명만 네트워크에 속해있지 않을 때
        elif (friendA_KEY == -1 and friendB_KEY!=-1) or (friendB_KEY == -1 and friendA_KEY!=-1):
            if friendA_KEY!=-1:
                friendNetwork[friendA_KEY]["friends"].append(friendB)
                friendNetwork[friendA_KEY]["count"] += 1
                print(friendNetwork[friendA_KEY]["count"])
            else:
                friendNetwork[friendB_KEY]["friends"].append(friendA)
                friendNetwork[friendB_KEY]["count"] += 1
                print(friendNetwork[friendB_KEY]["count"])
        
        # 같은 네트워크에 속해 있을 때
        elif friendA_KEY!=-1 and friendA_KEY == friendB_KEY:
            print(friendNetwork[friendA_KEY]["count"])
        
        # 다른 네트워크에 속해 있을 때
        elif  friendA_KEY!=-1 and friendA_KEY != friendB_KEY:
            friendNetwork[networkIdx] = dict()
            friendNetwork[networkIdx]["friends"] = friendNetwork[friendA_KEY]["friends"].extend(friendNetwork[friendB_KEY]["friends"])
            friendNetwork[networkIdx]["count"] = friendNetwork[friendA_KEY]["count"] + friendNetwork[friendB_KEY]["count"]
            print(friendNetwork[networkIdx]["count"])
            networkIdx += 1
