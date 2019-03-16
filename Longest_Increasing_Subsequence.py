class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        n = len(nums)
        if n <= 1:
            return n
        memo = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        ans = max(memo)
        return ans

t = Solution()
print(t.lengthOfLIS([1,3,6,7,9,4,10,5,6]))