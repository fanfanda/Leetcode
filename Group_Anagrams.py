import collections
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        res = collections.defaultdict(list)
        for item in strs:
            res[tuple(sorted(item))].append(item)
        
        return res.values()

t = Solution()
print(t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))