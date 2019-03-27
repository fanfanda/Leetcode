class Solution:    
    def find_kth(self, nums1, nums2, k):
        m, n  = len(nums1), len(nums2)
        if m > n: return self.find_kth(nums2, nums1, k)
        if m == 0: return nums2[k]
        if k == 1: return min(nums1[0], nums2[0])
        i = min(k//2, m)
        j = k - i
        if nums1[i - 1] < nums2[j - 1]: return self.find_kth(nums1[i:], nums2, k - j)
        return self.find_kth(nums1, nums2[j:], k - j)
# class Solution:
#     def findMedianSortedArrays(self, A, B):
#         m, n = len(A), len(B)
#         if m > n:
#             A, B, m, n = B, A, n, m
#         if n == 0:
#             raise ValueError

#         imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        
#         while imin <= imax:
#             i = int((imin + imax) / 2)
#             j = half_len - i
#             if i < m and B[j-1] > A[i]:
#                 imin = i + 1
#             elif i > 0 and A[i-1] > B[j]:
#                 imax = i - 1
#             else:
#                 if i == 0: max_of_left = B[j-1]
#                 elif j == 0: max_of_left = A[i-1]
#                 else: max_of_left = max(A[i-1], B[j-1])

#                 if (m + n) % 2 == 1:
#                     return max_of_left

#                 if i == m: min_of_right = B[j]
#                 elif j == n: min_of_right = A[i]
#                 else: min_of_right = min(A[i], B[j])

#                 return (max_of_left + min_of_right) / 2.0

a = [1, 3, 4]
b = [2, 5, 6, 8]

t = Solution()
print(t.find_kth(a, b, 7))