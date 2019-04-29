import math
class Solution:
    def FindContinuousSequence(self, tsum):
        '''和为S的连续正数序列'''
        res = []
        for div in range(2,int(math.sqrt(tsum * 2)) + 1):
            if (div%2 == 0 and tsum%div == div/2) or (div%2 == 1 and tsum%div == 0):
                start = tsum//div - div//2 + 1 if div%2==0 else tsum//div - div//2
                res.append(list(range(start, tsum//div + div//2 + 1)))
        return sorted(res, key = lambda x: x[0])