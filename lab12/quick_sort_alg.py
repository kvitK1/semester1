# def partition(lst, left, right):
#     '''
#     An additional function for def quick_sort to find the index of pivot.
#     '''
#     inx_i = left
#     inx_j = right-1
#     pivot = lst[right]
#     while inx_i < inx_j:
#         while inx_i < right and lst[inx_i] < pivot:
#             inx_i+=1
#         while inx_j > left and lst[inx_j] > pivot:
#             inx_j-=1
#         if inx_i < inx_j:
#             lst[inx_i], lst[inx_j] = lst[inx_j], lst[inx_i]
#     if lst[inx_i] > pivot:
#         lst[inx_i], lst[right] = lst[right], lst[inx_i]

#     return inx_i


# def quick_sort(lst, left=0, right=0):
#     '''
#     Return a sorted list.
#     '''
#     left = 0
#     right = len(lst)-1
#     if left < right:
#         partition_pos = partition(lst, left, right)
#         quick_sort(lst, left, partition_pos-1)
#         quick_sort(lst, partition_pos+1, right)
    
#     return lst

# print(quick_sort([34, 56, 12, 94, 103, 45, 3]))

def get_pivot(lst, low, high):
    middle = (low+high)//2
    pivot = high
    if lst[low] < lst[middle]:
        if lst[middle] < lst[high]:
            pivot = middle
    elif lst[low] < lst[high]:
        pivot = low

    return pivot


def partition(lst, low, high):
    pivot_inx = get_pivot(lst, low, high)
    pivot_value = lst[pivot_inx]
    lst[pivot_inx], lst[low] = lst[low], lst[pivot_inx]
    border = low
    for i in range(low, high+1):
        if lst[i] < pivot_value:
            border+=1
            lst[i], lst[border] = lst[border], lst[i]
    lst[low], lst[border] = lst[border], lst[low]

    return border


def quick_sort_2(lst, low, high):
    if low < high:
        pos = partition(lst, low, high)
        quick_sort_2(lst, low, pos-1)
        quick_sort_2(lst, pos+1, high)

    return lst


def quick_sort(lst):
    quick_sort_2(lst, 0, len(lst)-1)

    return lst

# print(quick_sort([45, 67, 23, 11, 98, 24]))

def Nmaxelements(list1, N):
    final_list = []
  
    for _ in range(0, N): 
        max1 = 0
          
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j];
                  
        list1.remove(max1);
        final_list.append(max1)
          
    print(final_list)
  
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
  
# Calling the function
Nmaxelements(list1, N)