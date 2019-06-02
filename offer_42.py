class Solution:
    def FindNumbersWithSum(self, array, tsum):
        '''和为S的两个数字'''
        low, high = 0, len(array) - 1
        while low < high:
            if array[low] + array[high] == tsum:
                return array[low], array[high]
            elif array[low] + array[high] > tsum:
                high -= 1
            else:
                low += 1
        return []