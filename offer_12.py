class Solution:
    def Power(self, base, exponent):
        '''数值的整数次方'''
        if base == 0: return 0
        if exponent == 0: return 1
        if exponent == 1: return base
        if exponent < 0: return self.Power(1/base, -exponent)
        mid = self.Power(base, exponent >> 1)
        if exponent % 2 == 0:
            return mid * mid
        else:
            return mid * mid * base