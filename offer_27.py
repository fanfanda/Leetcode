class Solution:
    def Permutation(self, ss):
        '''字符串的全排列'''
        if not ss: return []
        res = list()
        self.helper(ss, res, '')
        return sorted(list(set(res)))
    
    def helper(self, strs, res, path):
        if not strs:
            res.append(path)
        else:
            for i in range(len(strs)):
                self.helper(strs[:i] + strs[i + 1:], res, path + strs[i])
t = Solution()
print(t.Permutation('ab'))