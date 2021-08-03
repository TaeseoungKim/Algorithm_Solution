before_value = 5

def tmp():
    print(before_value)
    print(after_value)
    before_value = 50
    after_value = 100
    print(input_value)


after_value = 10

input_value = int(input())

tmp()