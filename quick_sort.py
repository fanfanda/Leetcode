
def quicksort_helper(nums, r, q):
    if r < q:
        k = partition(nums, r, q)
        quicksort_helper(nums, r, k)
        quicksort_helper(nums, k + 1, q)
def partition(nums, r, q):
    pivot = nums[r]
    while r < q:
        while r < q and nums[q] >= pivot:
            q -= 1
        if r < q:
            nums[r] = nums[q]
        while r < q and nums[r] < pivot:
            r += 1
        if r < q:
            nums[q] = nums[r]

    nums[r] = pivot
    return r

def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low
t = [2, 5, 7, 1, 0]
# quick_sort_standord(t, 0, len(t) - 1)