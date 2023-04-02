#mapping is used to add map the values with parameters
#for eg: list of dict. key values

double_num = []
numbers = (5,6,7,8,9)
for num in  numbers:
    double_num.append(num * 2)
print(double_num)


##using map
def double(num):
    return num*2

# double_List = list(map (double,numbers))
# print(double_List)
print(list(map (double,numbers)))
