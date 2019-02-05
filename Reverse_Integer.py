class Solution:
    def reverse(self, x: 'int') -> 'int':
        sign = 1 if x > 0 else -1
        reverse_num = int(str(x * sign)[::-1])

        return sign * reverse_num * (reverse_num < 2**31)

t = Solution()
print(t.reverse(4321))