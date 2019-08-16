# class Solution:
#     def ReverseSentence(self, s):
#         s = s.split(' ')
#         return ' '.join(s[::-1])

class Solution:
    def ReverseSentence(self, s):
        temp = s.split(' ')
        stacks, result = [], []
        for i in temp:
            stacks.append(i)
        while stacks:
            result.append(stacks.pop())
        return ' '.join(result)

t = Solution()
print(t.ReverseSentence('ffd zxz'))