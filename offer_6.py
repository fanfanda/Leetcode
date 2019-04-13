class Solution:
    def minNumberInRotateArray(self, rotateArray):
        '''在旋转数组中查找最小值'''
        n = len(rotateArray)
        if n <= 2: return min(rotateArray)
        if not n: return 0
        mid = n // 2
        if rotateArray[mid] < rotateArray[n - 1]: return self.minNumberInRotateArray(rotateArray[:mid + 1])
        else: return self.minNumberInRotateArray(rotateArray[mid + 1:])

t = Solution()
print(t.minNumberInRotateArray([4, 5, 1, 2, 3]))