# https://youtube.com/shorts/e-LUO2HeU1U?si=CfqRxX7Z-64muT0J


#return false if any of the number in array is more then twice

from collections import Counter

def twice(array):
    for i in array:
        array_count=array.count(i)
        print(f"count of {i} : {array_count}")
        if array_count > 2:
            return False
    return True # if all the number in array is less then twice  in arr
print(twice(array=[1,2,1,2,3,4,4]))


# yt solution
from collections import Counter

class Solution:
    def returnTrueifnotmorethen(self, nums):
        counter = Counter(nums)
        print(counter)
        for f in counter.values():
            print(counter.values())
            if f > 2:
                return False
        return True
    
solution = Solution()
print(solution.returnTrueifnotmorethen(nums=[1,2,1,2,3,4,4,4]))


###########################################################################################
# sort elements

list=[1,2,3,5,8,9,22,33,15,7]
size=len(list)

def sorting(list):
    for i in range(size):
        for j in range(size-1):
            if list[j] > list [j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

print(sorting(list))

###########################################################################################
# wo Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
'''

def two_sum(integer,target):
    for i in integer:
        for j in integer:
            if i+j == target:
                return [i,j]

integer = [7,2,8,5,3,10]
print(two_sum(integer,target=8))


###########################################################################################

'''Reverse a Linked List
'''

list1=[5,4,3,2,1]
list1.reverse()
print(f"reverse list : {list1}")

###########################################################################################

def first(func):
    def wrapper():
        print("first function")
        func()
        print("after middle function")
    return wrapper

@first
def use_dec():
    print("call decorator")
    
first(use_dec())
###########################################################################################





###########################################################################################