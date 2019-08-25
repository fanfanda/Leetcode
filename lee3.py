class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        max_lens, start, memo = 0, 0, {}
        for index, item in enumerate(s):
            if item in memo and memo[item] >= start:
                start = memo[item] + 1
            max_lens = max(max_lens, index - start + 1)
            memo[item] = index
        return max_lens
t = Solution()
print(t.lengthOfLongestSubstring('abba'))