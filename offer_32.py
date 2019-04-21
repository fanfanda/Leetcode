class Solution:
    def PrintMinNumber(self, numbers):
        '''数组中组合出最小的数字'''
        if not numbers: return ''
        
        numbers = list(map(str, numbers))
        numbers.sort(cmp = lambda x, y : cmp(x + y, y + x))
        return "".join(numbers)