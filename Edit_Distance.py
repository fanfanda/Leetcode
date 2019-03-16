class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(word1, word2):
            if (word1, word2) in memo:
                return memo[word1, word2]
            else:
                if not word1: return len(word2)
                if not word2: return len(word1)
                
                if word1[0] == word2[0]:
                    memo[word1, word2] = helper(word1[1:], word2[1:])
                else:
                    memo[word1, word2] = min(helper(word1[1:], word2), helper(word1[1:], word2[1:]), helper(word1, word2[1:])) + 1
                return memo[word1, word2]
        return helper(word1, word2)
    # def minDistance(self, word1: str, word2: str) -> int:
    #     if not word1: return len(word2)
    #     if not word2: return len(word1)
    #     if word1[0] == word2[0]:
    #         return self.minDistance(word1[1:], word2[1:])
    #     else:
    #         return min(self.minDistance(word1[1:], word2), self.minDistance(word1[1:], word2[1:]), self.minDistance(word1, word2[1:])) + 1

t = Solution()
print(t.minDistance('horse', 'ros'))