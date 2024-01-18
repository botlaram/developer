# ##selection sort


# def selection_sort(nums):
#     for i in range(nums):
#         if nums[i] > nums[i+1]:
#             # Swap the elements
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i + 1] = temp

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

if __name__=="__main__":
    print(selection_sort(nums))
