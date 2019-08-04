# from collections import defaultdict
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         '''数组中出现次数超过一半的数字'''
#         dicts, lens = defaultdict(int), len(numbers)//2
#         for i in numbers:
#             dicts[i] += 1
#             if dicts[i] > lens:
#                 return i
#         return 0

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        temp = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] != temp: count -= 1
            else: count += 1
            if not count: temp = numbers[i]; count = 1
        if count < 0: return 0
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == temp:
                count += 1
        return temp if count > len(numbers)//2 else 0

t = Solution()
print(t.MoreThanHalfNum_Solution([1, 2, 3, 2, 4, 2, 5, 2, 3]))
