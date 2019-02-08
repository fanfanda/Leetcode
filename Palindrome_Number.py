import math

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0: return False
        if x == 0: return True
        count = int(math.log10(x)) # 确定位数
        while(count > 0):
            high = int(x / (10 ** count)) # 最高位置
            low = x % 10 # 最低位置
            if high != low: 
                return False
            x = int(x % (10 ** count))
            x = int(x / 10)
            count -= 2
        return True

t = Solution()
print(t.isPalindrome(11))