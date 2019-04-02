def merge_sort(A):
    if len(A) <= 1: return A
    mid = len(A)//2
    left_sort = merge_sort(A[:mid])
    right_sort = merge_sort(A[mid:])
    return combine(left_sort, right_sort)

def combine(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: result.append(a[i]); i += 1
        else: result.append(b[j]); j += 1
    result += a[i:]; result += b[j:]
    return result
