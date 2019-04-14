class Solution:
    def jumpFloor(self, number):
        '''青蛙跳台阶'''
        memo = {}
        def helper(number):
            if number < 3: return number
            if number not in memo:
                memo[number] = helper(number - 1) + helper(number - 2)
            return memo[number]
        return helper(number)

t = Solution()
print(t.jumpFloor(15))