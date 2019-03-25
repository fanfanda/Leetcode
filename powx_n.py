class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 1
        if n == 0: return 1
        if n < 0: x = 1/x; n = -n
        half = self.myPow(x, n >> 1)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

t = Solution()
print(t.myPow(3, 0.1))