##filter is similar to mapping

nums_list = [1,2,3,4,5,6,7,8,9]
even=[]
for x in nums_list:
    if x % 2 == 0:
        even.append(x)
print(even)

#with filter
def even(x):
    return x%2==0
 
even_list= list(filter(even,nums_list))
print(even_list)


