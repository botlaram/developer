# Queue

from collections import deque
q=deque()

q.append(5)
q.appendleft(10)
q.appendleft(15)
q.appendleft(20)
q.appendleft(25)
q.appendleft(30)

print(q)
print(q.pop())
print(f"{q} after pop")
