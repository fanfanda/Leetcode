class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''自己实现pow平方函数, 利用二分法降低递归的深度'''
        if x == 0: return 1
        if n == 0: return 1
        if n < 0: x = 1/x; n = -n
        half = self.myPow(x, n >> 1)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

t = Solution()
print(t.myPow(1.00001, 123456))