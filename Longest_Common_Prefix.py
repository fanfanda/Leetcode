class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        result = ''
        for items in zip(*strs):
            if all(item == items[0] for item in items):
                result += items[0]
            else:
                return result
        return result
    
t = Solution()
print(t.longestCommonPrefix([""]))
# print(t.longestCommonPrefix(["flower","flow","flight"]))