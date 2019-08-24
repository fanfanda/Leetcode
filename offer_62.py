from heapq import heappush, nlargest, heappop
# result = []
# heappush(result, 4)
# heappush(result, 2)
# heappush(result, 5)
# print(nlargest(1, result)[-1])

class Solution:
    left = []
    right = []
    def Insert(self, num):
        if not self.right: self.right.append(num); return
        if len(self.left) == len(self.right):
            if num > self.right[0]: heappush(self.right, num)
            else: heappush(self.left, -num); maxs = -heappop(self.left); heappush(self.right, maxs)
        else:
            if num <= self.right[0]: heappush(self.left, -num)
            else: heappush(self.right, num); mins = heappop(self.right); heappush(self.left, -mins)
        
    def GetMedian(self, nums):
        if not self.left and not self.right: raise Exception('No element!')
        print(self.left, self.right)
        if len(self.left) == len(self.right): return (-self.left[0] + self.right[0])/2.0
        else: return self.right[0]


t = Solution()
t.Insert(5)
t.Insert(2)
# t.Insert(3)
# t.Insert(4)[5,2,3,4,1,6,7,0,8]

print(t.GetMedian([]))