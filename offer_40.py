class Solution:
    def FindNumsAppearOnce(self, array):
        '''数组中只出现一次的数字'''
        sums, index = 0, 0
        for item in array:
            sums ^= item
        while sums & 1 != 1:
            sums = sums >> 1
            index += 1
        a, b = 0, 0
        for item in array:
            if item >> index & 1:
                a ^= item
            else:
                b ^= item
        return a, b