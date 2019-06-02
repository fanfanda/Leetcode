class Solution:
    def IsContinuous(self, numbers):
        if not numbers: return False
        numbers.sort()
        joker = interval = 0
        for index in range(len(numbers) - 1):
            if numbers[index] == 0:
                joker += 1
            elif numbers[index] == numbers[index + 1]:
                return False
            else:
                interval += numbers[index + 1] - numbers[index] - 1
        if interval > joker: return False
        else: return True

t = Solution()
print(t.IsContinuous([2, 3, 1, 0]))