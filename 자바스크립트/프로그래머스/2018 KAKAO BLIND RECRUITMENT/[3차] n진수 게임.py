import math

# n	    t	m	p	result
# 2	    4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"


def encode():
    print()
    sequence = "0"
    n = 2
    # for i in range(t*m):  # 10진법 개수만큼
    for i in range(1, 14+1):
        square = math.ceil(math.sqrt(IndentationError))
        value = i
        tempSequence = ""
        print("i: ", i)

        while True:
            if value//(n**square) > 0:
                tempSequence = str(value//(n**square)) + tempSequence
                square += 1
                value = value % (n**square)
            else:

                break

        sequence += tempSequence
        print("sequence: ", sequence)
    print(sequence)


encode()


def solution(n, t, m, p):
    answer = ''
    return answer
