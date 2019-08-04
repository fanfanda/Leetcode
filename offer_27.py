# class Solution:
#     def Permutation(self, ss):
#         '''字符串的全排列'''
#         if not ss: return []
#         res = list()
#         self.helper(ss, res, '')
#         return sorted(list(set(res)))
    
#     def helper(self, strs, res, path):
#         if not strs:
#             res.append(path)
#         else:
#             for i in range(len(strs)):
#                 self.helper(strs[:i] + strs[i + 1:], res, path + strs[i])



class Solution:
    def Permutation(self, ss):
        self.result = []
        self.helper(ss, '')
        return sorted(list(set(self.result)))

    def helper(self, ss, res):
        if not ss: self.result.append(res)
        for i in range(len(ss)):
            self.helper(ss[:i] + ss[i + 1:], res + ss[i])

t = Solution()
print(t.Permutation('ab'))