class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        lens = len(nums)
        low, high = 0, lens - 1

        while low <= high:
            mid = (low + high) // 2
            # print(nums[low:high + 1], nums[mid])
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]: # 注意low/mid/high 可能是同一个坐标
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

t = Solution()
print(t.search([3, 1], 1))