class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

t = Solution()
print(t.maxSubArray([1, 2, 3]))