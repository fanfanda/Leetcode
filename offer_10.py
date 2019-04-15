class Solution:
    def rectCover(self, number):
        '''矩形覆盖'''
        memo = {}
        def helper(number):
            if number <= 2:
                return number
            if number not in memo:
                memo[number] = helper(number - 2) + helper(number - 1)
            return memo[number]
        return helper(number)
