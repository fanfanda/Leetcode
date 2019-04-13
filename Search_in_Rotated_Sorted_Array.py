class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        '''旋转数组查找数字'''
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]: return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]: low = mid + 1
                else: high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]: high = mid - 1
                else: low = mid + 1
        return -1
# class Solution:
#     def search(self, nums: 'List[int]', target: int) -> int:
#         lens = len(nums)
#         low, high = 0, lens - 1

#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target: return mid
#             if nums[low] <= nums[mid]:
#                 if nums[low] <= target <= nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if nums[mid] <= target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         return -1

t = Solution()
print(t.search([3, 1], 1))