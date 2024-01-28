# ###quick sort use pivot (to select initial pivot number)

# def quicksort(my_list):
#     if len(my_list) <= 1:
#         return my_list
#     else:
#         pivot = my_list[0]
#         lesser = [x for x in my_list[1:] if x <= pivot]
#         greater = [x for x in my_list[1:] if x > pivot]
#         return quicksort(lesser) + [pivot] + quicksort(greater)

# # Example usage:
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# quicksort = quicksort(my_list)
# print(quicksort)



# try by your own

def quick_sort(nums):
    if len(nums)<=1:
        return nums
    else:
        pivot=nums[0]
        lesser=[]
        greater=[]
        for x in nums[1:]:
            if x < pivot:
                lesser.append(x)
        for x in nums[1:]:
            if x > pivot:
                greater.append(x)
                
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
nums=[22,11,88,66,55,77,33,44]
if __name__=="__main__":
    print(quick_sort(nums))
    