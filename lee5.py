class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        max_res = s[0]
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            memo[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                memo[i][i + 1] = True
                max_res = s[i: i + 2]

            for i in range(3, len(s) + 1):
                for j in range(len(s) - i + 1):
                    if s[j] == s[j + i - 1] and memo[j + 1][j + i - 2]:
                        memo[j][j + i - 1] = True
                        max_res = s[j:j + i]
                    
        return max_res
t = Solution()
print(t.longestPalindrome("civilwartestin"))