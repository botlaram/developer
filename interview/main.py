import copy 

list =[1,[2,3,4],5]

shallow_copy=copy.copy(list)
shallow_copy[1][0]="x"

print(shallow_copy)
print(list)

list2=[6,[7,8,9],10]
deep_copy=copy.deepcopy(list2)
deep_copy[1][0]="y"

print(list2)
print(deep_copy)