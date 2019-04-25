class Solution:
    def GetNumberOfK(self, data, k):
        '''统计一个数字在排序数组中出现的次数'''
        first = self.find_help(data, k, True)
        last = self.find_help(data, k, False)
        if first != -1:
            return last - first + 1
        return 0
    def find_help(self, data, k, sign):
        low, high, lens = 0, len(data) - 1, len(data)
        while low <= high:
            mid = (low + high)//2
            if data[mid] == k:
                if sign:
                    if (mid > 0 and data[mid - 1] != k) or mid == 0: return mid
                    else: high = mid - 1
                else:
                    if mid < lens - 1 and data[mid + 1] != k or mid == lens - 1: return mid
                    else: low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return -1
t = Solution()
print(t.GetNumberOfK([3, 3, 3, 3, 4, 5], 3))