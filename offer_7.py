class Solution:
    def Fibonacci(self, n):
        memo = {}
        def helper(n):
            if n <= 1: return n
            if n not in memo:
                memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]
        return helper(n)

t = Solution()
print(t.Fibonacci(3))