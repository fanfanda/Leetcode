class Solution:
    def ReverseSentence(self, s):
        s = s.split(' ')
        return ' '.join(s[::-1])

t = Solution()
t.ReverseSentence('ffd zxz')