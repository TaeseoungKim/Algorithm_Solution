
from collections import deque


deq1 = deque([1,[0]])
deq2 = deque((1,0))
deq3 = deque()

deq3.append((1,0))
deq3.append((1,0))

print(deq1.pop())
print(deq1.pop())
print(deq2.pop())
print(deq3.pop())