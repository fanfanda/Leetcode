class Solution:
    def twoSum(self, nums, target):
        temp_dict = {}

        for index, item in enumerate(nums):
            try:
                return [index, temp_dict[target - item]]
            except KeyError:
                temp_dict[item] = index

        # temp_dict = {}

        # for index, item in enumerate(nums):
        #     temp_dict[item] = index
        
        # for index, item in enumerate(nums):
        #     try:
        #         if index != temp_dict[target - item]:
        #             return [index, temp_dict[target - item]]
        #     except KeyError:
        #         continue

nums = [2, 7, 11, 15]
target = 9

t = Solution()
print(t.twoSum(nums, target))