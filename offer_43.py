class Solution:
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def LeftRotateString(self, s, n):
        '''左旋转字符串'''
        if not s: return s
        s = list(s)  #str转成list处理
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)  #直接join列表就变成str了