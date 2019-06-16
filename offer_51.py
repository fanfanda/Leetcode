class Solution:
    def match(self, s, pattern):
        if s == pattern:
            return True
        if not pattern:
            return False
        if len(pattern)>1 and pattern[1] == '*':
            if(s and s[0]==pattern[0]) or (s and pattern[0] == '.'):
                return self.match(s,pattern[2:]) \
                    or self.match(s[1:],pattern) \
                    or self.match(s[1:],pattern[2:])
            else:
                return self.match(s,pattern[2:])
        elif s and (s[0] == pattern[0] or pattern[0]=='.'):
                return self.match(s[1:],pattern[1:])
        return False