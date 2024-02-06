## simple stack function (LIFO=Last In First Out)

### stack using list
s=[]
s.append("https://google.com")
s.append("https://google.com/facebook")
s.append("https://google.com/feeds")
s.append("https://google.com/photos")
print(s)
print(s.pop())
print(s.pop())
print(s)


### stack using deque (this is recommended)
from collections import deque

stack=deque()
print(type(stack))
stack.append("https://google.com")
stack.append("https://google.com/facebook")
stack.append("https://google.com/feeds")
stack.append("https://google.com/photos")
print(stack)
print(stack.pop())
print(stack.pop())
stack.append("https://wikipedia.com")
print(stack)