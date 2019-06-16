class Solution:
    def Sum_Solution(self, n):
        return n > 0 and n + self.Sum_Solution(n - 1)

t = Solution()
print(t.Sum_Solution(10))