class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        lens = len(nums)
        best = nums[0] + nums[1] + nums[2]
        for i in range(lens - 2):
            left, right = i + 1, lens - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target: return total
                if abs(total - target) < abs(best - target):
                    best = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return best

t = Solution()
print()