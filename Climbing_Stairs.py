class Solution:
    def climbStairs(self, n: int) -> int:
        temp_dict = {}
        temp_dict[1] = 1
        temp_dict[2] = 2
        if n < 3:   return temp_dict[n]
        for i in range(3, n + 1):
            temp_dict[i] = temp_dict[i - 1] + temp_dict[i - 2]
        return temp_dict[n]

    # def climbStairs(self, n: int) -> int:
    #     if n == 1:  return 1
    #     if n == 2:  return 2
    #     else:
    #         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


t = Solution()
print(t.climbStairs(3))