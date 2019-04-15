class Solution:
    def reOrderArray(self, array):
        '''奇数在前，偶数在后'''
        l1 = list(filter(lambda x: x % 2, array))
        l2 = list(filter(lambda x: x % 2 == 0, array))
        return l1 + l2

t = Solution()
print(t.reOrderArray([1, 2, 3, 4, 5]))