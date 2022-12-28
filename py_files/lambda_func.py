##without lambda
def add(x,y):
    print(x+y)
add(2,5)


#using lambda
add = lambda x,y:x+y
print(add(2,5))

#passing argument without lambda
nums=[2,4,6,8,10]
def mul(x):
    for i in x:
        i=i*2
        print(i,end=" ")
mul(nums)


##passing argument in lambda using map
doubled_map = list(map(lambda x: x*2,nums))
print(doubled_map)