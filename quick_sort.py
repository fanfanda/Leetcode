def quick_sort(A, left, right):
    if left < right:
        k = partition(A, left, right)
        quick_sort(A, left, k)
        quick_sort(A, k + 1, right)
    
def partition(A, left, right):
    pivot = A[left]
    while left < right:
        while left < right and A[right] > pivot: right -= 1
        if left < right: A[left] = A[right]
        while left < right and A[left] < pivot: left += 1
        if left < right: A[right] = A[left]
    A[left] = pivot 
    return left
t = [2, 5, 7, 1, 0]
# quick_sort_standord(t, 0, len(t) - 1)