#factorial [5! = 5*4*3*2*1]
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(5))

##factorial [5! = 5*4*3*2*1](using recursion)
def fact(n):
    if n==0:
        return 1
    print(n)
    return n*fact(n-1)
print(fact(6))

#palindrome (nitin==nitin)
# we can check palindrome by reversing str

str1="nitin"
str2=str1[::-1]
if str1 == str2:
    print("palindrome")
else:
    print("not a palindrome")

#generator
def generator():
    for i in range(10):
        yield i

for i in generator():
    print(i)

import re

match=re.search(r'krishna',"myself rama krishna")
print(match)
print(match.group())
