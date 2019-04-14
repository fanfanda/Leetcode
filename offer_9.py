class Solution:
    def jumpFloorII(self, number):
        '''变态青蛙跳台阶'''
        memo = {}
        temp = 0
        for i in range(1, number + 1):
            if i == 1: memo[i] = i
            else: memo[i] = temp + 1
            temp += memo[i]
        return memo[i]

t = Solution()
print(t.jumpFloorII(5))