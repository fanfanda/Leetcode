class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: return -self.reverse(-x)
        res, maxint = 0, ((2 << 30) - 1)
        minint = -(maxint + 1)
        while x:
            pop = x % 10
            x //= 10
            if (res > maxint / 10) or (res == maxint // 10 and pop > 7): return 0
            res = res * 10 + pop
        return res
t = Solution()
print(t.reverse(-123))