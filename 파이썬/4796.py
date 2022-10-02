import sys
input = sys.stdin.readline
case_cnt = 0
while(True):
    case_cnt += 1
    
    L, P, V = map(int, input().split())
    # L,P,V가 모두 0일 시, 프로그램 종료
    if L == 0 and P == 0 and V == 0: 
        break

    # 총 휴가를 P로 나누고, 사용가능 한 일 수인 L * 몫을 result에 저장한다 
    quotient = V // P
    result = quotient * L

    # 남은 휴가가 L보다 클 경우 L을 result에 더해주고,
    # 작을 경우 남은 휴가를 result에 더해준다.
    if V - (quotient * P) > L:
        result += L
    else:
        result += V - (quotient * P)
    print("Case %d:"%case_cnt,result)