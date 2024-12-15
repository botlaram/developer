# selection sort

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
print(f"without sorting {nums}")

if __name__=="__main__":
    print(selection_sort(nums))
