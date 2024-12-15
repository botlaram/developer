# # num=17

# # for i in range(2,num//2):
# #     print(i)
# #     if num % i == 0:
# #         print(f"not prime : {i}")
# # else:
# #     print(num,"prime")

# dict={"ram":25,"hari":20}

# print(dict.get("ram"))
# print(dict["ram"])

# dict.update([{"new",30},{"new1",40}])
# print(dict, "using update")

# dict["city"]="mumbai"
# print(dict,"add city")


# dict.pop("ram")
# print(dict,"delete dict")

# dict.popitem()
# print(dict,"delete last element using popitem()")

# print(dict.keys())
# print(dict.values())
# for i, j in dict.items():
#     print(i,j)

# dict2 = {'b': 3, 'c': 4}
# dict.update(dict2)
# print(dict)


# #dict comprehension
# # {key_expression: value_expression for item in iterable if condition}
# square={x:x**2 for x in range(10) if x%2!=0}
# print(square)

# dict.clear()
# print(dict,"clear dict")


 
# from enum import Enum
 
# class Season(Enum):
#     SPRING = 1
#     SUMMER = 2
#     AUTUMN = 3
#     WINTER = 4

# print(Season.SPRING.value)

'''
Reverse Words in a Sentence
Question: Write a Python function that takes a string sentence and returns the sentence 
with the words reversed. The order of the characters in each word should remain the same, 
but the order of the words should be reversed.
'''

# input = "Hello world this is Python"

# output=input.split()[::-1]
# print(output)

'''
Find the Longest Substring Without Repeating Characters
Question: Write a function to find the length of the longest substring of a given string that does not contain any repeating characters.
'''

# input="abcabefghicbb"
# output=""
# for i in range(0,len(input)-1):
#     if input[i] != input[i+1] and input[i] not in output:
#         output=''.join((output,input[i]))
# print(len(output))
    
'''
4. Find All Anagrams in a List of Words
Question: Given a list of words, write a function that groups the words into anagrams. 
Two words are anagrams if they contain the same characters with the same frequency.
'''

Input=["eat", "tea", "tan", "ate", "nat", "bat"]
list=[]
for i in range(0,len(Input)-1):
    if Input[i] in Input[i+1]:
        list.append(Input[i])
print(list)

'''
decorator in python
'''

def dec(parameter):
    def inside():
        print("do step 1")
        parameter()
        print("do step2")
    return inside

@dec
def external():
    print("additional function")
    
external()
    
'''
class
'''

class Org():
    
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
        
    def details(self):
        return self.name
        
class inherit(Org):
    
    def __init__(self, name, id, joining) -> None:
        super().__init__(name, id)
        self.joining=joining
        
    def join_Date(self):
        return self.joining

obj=inherit("ram","123",1456789)
print(obj.name)
print(obj.join_Date())

'''
Write a Python function to find the second largest number in a list.
'''

# num=[1,2,3,4,5,6,7,8,9]

# num.reverse()
# print(num[1])

'''
selection sort
'''



def selection_sort(nums):
    size=len(nums)
    
    for i in range(size):
        min=i
        for j in range(i,size):
            if nums[min] > nums[j]:        
                min=j
        nums[i],nums[min]=nums[min],nums[i]
    return nums
nums=[4,9,6,8,12,56,85,47,3,10]

print(selection_sort(nums))
