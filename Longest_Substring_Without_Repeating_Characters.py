class Solution:
    def lengthOfLongestSubstring(self, s):
        ans = start = 0
        temp_dict = {}
        
        for index, item in enumerate(s):
            if item in temp_dict.keys():
                start = max(temp_dict[item], start)
            ans = max(ans, index - start + 1)
            temp_dict[item] = index + 1
        return ans

s = "abcabcbb"

t = Solution()
print(t.lengthOfLongestSubstring(s))