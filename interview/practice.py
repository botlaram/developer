# num=17

# for i in range(2,num//2):
#     print(i)
#     if num % i == 0:
#         print(f"not prime : {i}")
# else:
#     print(num,"prime")

dict={"ram":25,"hari":20}

print(dict.get("ram"))
print(dict["ram"])
dict.update([{"new",30},{"new1",40}])
print(dict, "using update")

dict["city"]="mumbai"
print(dict,"add city")


dict.pop("ram")
print(dict,"delete dict")

dict.popitem()
print(dict,"delete last element using popitem()")

print(dict.keys())
print(dict.values())
for i, j in dict.items():
    print(i,j)

dict2 = {'b': 3, 'c': 4}
dict.update(dict2)
print(dict)


#dict comprehension
# {key_expression: value_expression for item in iterable if condition}
square={x:x**2 for x in range(10) if x%2!=0}
print(square)

dict.clear()
print(dict,"clear dict")


 
from enum import Enum
 
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(Season.SPRING.value)