class Solution:
    def replaceSpace(self, s):
        # 替换空格
        temp = s.split(' ')
        return '%20'.join(temp)

t = Solution()
print(t.replaceSpace("123 342"))