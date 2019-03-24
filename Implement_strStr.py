class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''KMP算法'''
        i, j = 0, 0
        get_next = self.get_next(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j =  get_next[j]
        if j == len(needle): return i - j
        else: return -1
    
    def get_next(self, p):
        res = [-1 for i in range(len(p))]
        i, j = 0, -1
        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                j += 1
                i += 1
                res[i] = j
            else:
                j = res[j]
        return res

t = Solution()
print(t.strStr('abcdef', 'ghi'))


# def strStr(self, haystack: str, needle: str) -> int:
    #     '''brute-force'''
    #     i, j = 0, 0
    #     while i < len(haystack) and j < len(needle):
    #         if haystack[i] == needle[j]:
    #             i += 1
    #             j += 1
    #         else:
    #             i = i - j + 1
    #             j = 0 
    #     if j == len(needle): return i - j
    #     else: return -1