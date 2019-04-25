class Solution:
    def GetUglyNumber_Solution(self, index):
        '''丑数'''
        if index < 7: return index
        res = [1, ]
        m1 = m2 = m3 = 0
        for i in range(1, index):
            num2, num3, num5 = res[m1] * 2, res[m2] * 3, res[m3] * 5
            mins = min(num2, num3, num5)
            res.append(mins)
            while res[m1] * 2 <= mins:
                m1 += 1
            while res[m2] * 3 <= mins:
                m2 += 1
            while res[m3] * 5 <= mins:
                m3 += 1
        return res[index - 1]