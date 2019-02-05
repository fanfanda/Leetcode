class Solution:
    def longestPalindrome(self, s):
        start = end = 0

        for index in range(len(s)):
            len1 = self.expandAroundCenter(s, index, index)
            len2 = self.expandAroundCenter(s, index, index + 1)

            temp_len = max(len1, len2)
            if temp_len > (end - start):
                start = index - int((temp_len - 1) / 2)
                end = index + int(temp_len / 2)
        return s[start:end + 1]

    def expandAroundCenter(self, s, start, end):
        L, R = start, end
        while (L >= 0 and R < len(s) and (s[L] == s[R])):
            L -= 1
            R += 1
        return R - L - 1

    

s = "ffddff"
t = Solution()
print(t.longestPalindrome(s))