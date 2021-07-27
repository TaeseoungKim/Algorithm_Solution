# 10994 별찍기
"""
4
*************
*           *
* ********* *
* *       * *
* * ***** * *
* * *   * * *
* * * * * * *
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************

"""
number = int(input())

# 가운데를 기준으로 top과 bottom을 나눈다
top = number
bottom = 0


# 입력받은 number가 1일시에 *출력
if number == 1:
    print("*")
else:
    for i in range(number):  # 반복문을 시작하며 i는 1씩 증가하고, top의 값은 1씩 감소한다

        if i == number-1:    # 반복문의 마지막, 즉 가운데 처리
            print("*", end="")  # 맨 왼쪽 하나 부여해줌

            for left in range(2*i):
                print(" *", end="")

            print(" ")
        else:
            print("*", end="")  # 맨 왼쪽 하나 부여해줌

            for left in range(i):
                print(" *", end="")

            for middle in range((top-1)*4-1):  # 양 옆의 star를 뺀 개수는 (top-1)*4-1
                print("*", end="")

            print("*", end="")  # middle의 오른쪽 끝을 하나 채워준다.

            for left in range(i):
                print(" *", end="")

            print(" ")

            print("*", end="")  # 맨 왼쪽 하나 부여해줌

            for left in range(i):
                print(" *", end="")

            for middle in range((top-1)*4-1):
                print(" ", end="")

            print("*", end="")  # middle의 오른쪽 끝을 하나 채워준다.

            for left in range(i):
                print(" *", end="")

            print(" ")
           # print("top %d"%top)

        top -= 1

    bottom = top+2
#    print("bottom %d"%bottom)
    for i in range(number-2, -1, -1):

        print("*", end="")  # 맨 왼쪽 하나 부여해줌

        for left in range(i):
            print(" *", end="")

        for middle in range((bottom-1)*4-1):
            print(" ", end="")

        print("*", end="")  # middle의 오른쪽 끝을 하나 채워준다.

        for left in range(i):
            print(" *", end="")

        print(" ")

        print("*", end="")  # 맨 왼쪽 하나 부여해줌

        for left in range(i):
            print(" *", end="")

        for middle in range((bottom-1)*4-1):
            print("*", end="")

        print("*", end="")  # middle의 오른쪽 끝을 하나 채워준다.

        for left in range(i):
            print(" *", end="")

        if i != 0:
            print(" ")
        else:
            print("")

        bottom += 1
