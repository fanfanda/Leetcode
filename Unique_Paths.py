class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for j in range(n)] for i in range(m)]
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                memo[j][i] = memo[j + 1][i] + memo[j][i + 1]
        return memo[0][0]

t = Solution()
print(t.uniquePaths(3, 4))