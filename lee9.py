class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        reverse_number, temp = 0, x

        while temp:
            reverse_number = reverse_number * 10 + temp % 10
            temp //= 10
        return reverse_number == x
t = Solution()
print(t.isPalindrome(121))