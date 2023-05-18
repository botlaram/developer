#list comprehension
#the simply readable way of transforming elements in list
#either by mapping or filtering

nums_List=[5,6,7,8]

##listcomprehension for maping
mapping = list(x*2 for x in nums_List)
print(mapping)

##listcomprehension for filtering
filtering = list(x for x in nums_List if x%2==0)
print(filtering)