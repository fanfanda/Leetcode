from collections import defaultdict
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        '''数组中出现次数超过一半的数字'''
        dicts, lens = defaultdict(int), len(numbers)//2
        for i in numbers:
            dicts[i] += 1
            if dicts[i] > lens:
                return i
        return 0