class Solution:
    def StrToInt(self, s):
        if not s:
            return 0

        num, sign = 0, 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]; sign = -1
        while s:
            if s[0] <= '9' and s[0] >= '0':
                num = num * 10 + int(s[0])
                s = s[1:]
            else:
                return 0
        return sign * num

t = Solution()
print(t.StrToInt('1a33'))