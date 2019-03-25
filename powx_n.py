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
# class Solution:
#     def myPow(self, a, b):
#         if b == 0: return 1
#         if b < 0: return 1.0 / self.myPow(a, -b)
#         half = self.myPow(a, b // 2)
#         if b % 2 == 0:
#             return half * half
#         else:
#             return half * half * a

t = Solution()
print(t.myPow(3, 0.1))