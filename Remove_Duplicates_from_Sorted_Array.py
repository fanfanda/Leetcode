class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if not nums: return 0
        first = 0
        for item in range(1, len(nums)):
            if nums[item] != nums[first]:
                first += 1
                nums[first] = nums[item]
        return first + 1

t = Solution()
nums = [1, 1, 2]
print(t.removeDuplicates(nums))