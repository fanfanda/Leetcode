from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: raise EOFError; return 
        memo = {}
        for index, item in enumerate(nums):
            if target - item in memo.keys():
                return index, memo[target - item]
            memo[item] = index
        return 

t = Solution()
print(t.twoSum([1, 2, 5], 3))