from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_left = (len(nums1) +len(nums2) + 1) // 2
        min_right = (len(nums1) +len(nums2) + 2) // 2
        return (self.find_k(nums1, nums2, max_left) + self.find_k(nums1, nums2, min_right)) / 2.0

    def find_k(self, nums1, nums2, k):
        
        if len(nums1) > len(nums2): return self.find_k(nums2, nums1, k)
        if not nums1: return nums2[k - 1] 
        if k == 1: return min(nums1[0], nums2[0])

        p1 = min(len(nums1), k//2) - 1
        p2 = k - p1 - 2
        print(nums1, nums2, k, p1, p2)

        if nums1[p1] < nums2[p2]: return self.find_k(nums1[p1 + 1:], nums2, k - p1 - 1)
        else: return self.find_k(nums1, nums2[p2 + 1:], k - p2 - 1)

t = Solution()
print(t.find_k([1, 3, 5], [2, 4, 6], 3))