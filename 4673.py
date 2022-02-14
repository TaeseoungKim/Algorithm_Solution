def self_num(n):
    non_self = []
    self = list(range(1,10001))
    for i in range(n):
        sum = i
        for c in str(i):
            sum += int(c)
        non_self.append(sum)
    print(*sorted(list(set(self)-set(non_self))),sep='\n')

self_num(10000)