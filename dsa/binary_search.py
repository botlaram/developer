# ##binary search can be implemented if elements are in sorted
# #if elements are not sorted, then we need to sort elements then implement binary search

# # binary search
def binary_search(arr, target):
    low, high = 0, len(arr)

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return f"found at index {mid}"  # Target found, return the index
        elif mid_val < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# # Example usage:
sorted_array = [11,15, 22, 38, 42, 68, 71, 89, 90,101]
target_value = 11

print(binary_search(sorted_array,target_value))

