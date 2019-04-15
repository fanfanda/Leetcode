class Solution:
    def NumberOf1(self, n):
        '''二进制中1的个数'''
        temp, count = 1, 0
        
        for i in range(32):
            if temp & n != 0:
                count += 1
            temp = temp << 1
        return count