# Example lists
list1=[3,45,85,7,8,9,6,555,69,9,32,76,89,14,20,35,79,99]

## add value at last
list1.append(5)
print("append : ",list1)

##copy list to other variable
x=list.copy(list1)
print("copy : ",x)

##count the repeated numbers
print("count : ",list1.count(9))

##length of list
print("len : ",len(list1))

##extend (use for adding iterable list to current list)
list1.extend([6546,8,9])
print("extend : ",list1)

##index
print("index : ",list1.index(6546))

##insert(index,value)
list1.insert(1,1000)
print("insert : ",list1)

##pop (it will remove by using index element)
list1.pop(-1)
print("pop : ",list1)

##remove (it will remove by using value element)
list1.remove(8)
print("remove : ",list1)

##reverse
list1.reverse()
print("reverse : ", list1)

##sort
list1.sort(reverse=True)
print("sorted : ", list1)

##sum
print("sum : ",sum(list1))

##min
print("min : ",min(list1))

##max
print("max :",max(list1))

##clear
list1.clear()
print("clear : ",list1)
