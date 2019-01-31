class Solution:
    def lengthOfLongestSubstring(self, s):
        temp_dict = {}
        for index, item in enumerate(s):
            if item not in temp_dict.keys():
                pass
        return 1

s = "pwwkew"

t = Solution()
print(t.lengthOfLongestSubstring(s))