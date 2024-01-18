#bubble sort
def bubble_sort(list):
    size=len(list)
    for i in range(size-1):
        for j in range(size-1):  # -1 because we dont need to compare with last element of the list
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]  #swap nums
        print(list)
    return list
list=[1,89,468464,8468,48648,4684,68,468,462,13,5]

if __name__ == '__main__':
    bubble=bubble_sort(list)
    print(bubble,"\n")


#### execute using cProfile module for time estimation
#bubble sort
import cProfile
def bubble_sort_time(list):
    size=len(list)
    for i in range(size-1):
        for j in range(size-1):  # -1 because we dont need to compare with last element of the list
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]  #swap nums
        print(list)
    # return list
    print(list)
list=[1,89,468464,8468,48648,4684,68,468,462,13,5]

if __name__ == '__main__':
    cProfile.run('bubble_sort_time(list)')






