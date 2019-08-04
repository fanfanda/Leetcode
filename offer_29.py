# from heapq import *
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         '''数组前k个最小的'''
#         if k > len(tinput):
#             return []
#         heapify(tinput)
#         res = []
#         for i in range(k):
#             res.append(heappop(tinput))
#         return res

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n: return []
        left = 0
        right = n - 1
        mid = self.partition(tinput, left, right)
        while k - 1 != mid:
            if k - 1 > mid:
                left = mid + 1
                mid = self.partition(tinput, left, right)
            elif k - 1 < mid:
                right = mid - 1
                mid = self.partition(tinput, left, right)
        res = tinput[:mid + 1]
        return sorted(res)

    def partition(self, numbers, low, high):
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        return low
    # def partition(self, A, left, right):
    #     pivot = A[left]
    #     while left < right:
    #         while left < right and A[right] > pivot:
    #             right -= 1
    #         A[left] = A[right]
    #         while left < right and A[left] <= pivot:
    #             left += 1
    #         A[right] = A[left]
    #     A[left] = pivot
    #     return left

# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         n = len(tinput)
#         if k <= 0 or k > n:
#             return list()
#         start = 0
#         end = n - 1
#         mid = self.partition(tinput, start, end)
#         while k - 1 != mid:
#             if k - 1 > mid:
#                 start = mid + 1
#                 mid = self.partition(tinput, start, end)
#             elif k - 1 < mid:
#                 end = mid - 1
#                 mid = self.partition(tinput, start, end)
#         res = tinput[:mid+1]
#         # res.sort()
#         return sorted(res)
        
#     def partition(self, numbers, low, high):
#         key = numbers[low]
#         while low < high:
#             while low < high and numbers[high] >= key:
#                 high -= 1
#             numbers[low] = numbers[high]
#             while low < high and numbers[low] <= key:
#                 low += 1
#             numbers[high] = numbers[low]
#         numbers[low] = key
#         return low

t = Solution()
print(t.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],1))