from heapq import *
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        '''数组前k个最小的'''
        if k > len(tinput):
            return []
        heapify(tinput)
        res = []
        for i in range(k):
            res.append(heappop(tinput))
        return res