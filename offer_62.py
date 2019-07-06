from heapq import heappush, nlargest
# result = []
# heappush(result, 4)
# heappush(result, 2)
# heappush(result, 5)
# print(nlargest(1, result)[-1])

class Solution:
    nums = []
    def Insert(self, num):
        heappush(self.nums, num)

    def GetMedian(self, nums):
        size = len(self.nums)
        if size % 2 != 0:
            return nlargest(size//2 + 1, self.nums)[-1]
        else:
            return (nlargest(size//2, self.nums)[-1] + nlargest(size//2 + 1, self.nums)[-1])/2

t = Solution()
# t.Insert(3)
t.Insert(5)
t.Insert(2)
# t.Insert(4)

print(t.GetMedian([5, 2]))