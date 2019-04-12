class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        temp = s.split(' ')
        return '%20'.join(temp)
        # return s

t = Solution()
print(t.replaceSpace("123 342"))