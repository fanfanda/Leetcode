class Solution:
    # dp version
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        '''
        memo[i, j] represents whether s[i:], p[j:] match.
        '''
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                # calculate memo[i, j]
                # memo[i, j] = ans
                if j == len(p): 
                    ans = i == len(s)
                else:
                    match = i < len(s) and p[j] in {s[i], '.'}
                    if j < len(p) - 1 and p[j + 1] == '*':
                        ans = match and dp(i + 1, j) or dp(i, j + 2)
                    else:
                        ans = match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

    # recursive version   
    # def isMatch(self, s: 'str', p: 'str') -> 'bool':
    #     if not p: return not s # base case
        
    #     match = bool(s) and p[0] in {s[0], '.'}

    #     if len(p) > 1 and p[1] == '*':
    #         return match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) # *要么消除前一个字符, 要么
    #     else:
    #         return match and self.isMatch(s[1:], p[1:])

t = Solution()
print(t.isMatch("aa", "aa*"))