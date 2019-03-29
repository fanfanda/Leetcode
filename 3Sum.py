class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        nums.sort()
        lens = len(nums)
        for i in range(lens - 2):
            if i != 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            left, right = i + 1, lens - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # print(i, left, right, 'sum', total)
                # print(nums)
                # print(nums[i], nums[left], nums[right], 'sum', total)
                # print('----------------------')
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

t = Solution()
print(t.threeSum([-1,0,1,2,-1,-4]))