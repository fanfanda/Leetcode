class Solution:
    def FindGreatestSumOfSubArray(self, array):
        '''连续子数组的最大和'''
        res = max_res = 0
        for item in array:
            res += item
            if res < 0: res = 0
            max_res = max(max_res, res)
        
        if not max_res: return max(array)
        return max_res

t = Solution()
print(t.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))