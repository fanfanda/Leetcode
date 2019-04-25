from collections import defaultdict
class Solution:
    def FirstNotRepeatingChar(self, s):
        '''第一次只出现一次的字符'''
        memo = defaultdict(int)
        for item in s:
            memo[item] += 1
        for index, item in enumerate(s):
            if memo[item] == 1:
                return index
        return -1
t = Solution()
print(t.FirstNotRepeatingChar('google'))