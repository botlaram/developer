##linear search

def searching(lst,search_ele):
    for i in range(len(lst)):     #here i will be index value i.r=e[0,1,2,3,4]
        if lst[i] == search_ele:    #here lst[i] will be value fetching from index i.e lst[0],lst[1]
            return True
    return False
    
elements=[100,55,66,251,684684,64868,4684,6,6846,684684,848]
target=66

print(searching(elements,target))


## find index of target element using list comprehension
x = [i for i in range(len(elements)) if target == elements[i]]
print(x)