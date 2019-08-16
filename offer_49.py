class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for index in range(len(numbers)):
            if index != numbers[index] and numbers[index] == numbers[numbers[index]]:
                duplication[0] = numbers[index]
                return True
            else:
                numbers[numbers[index]] = numbers[index]
        return False

t = Solution()
print(t.duplicate([0, 2, 4, 4, 1, 3], [-1]))
# print(t.duplicate([2, 1, 3, 0, 4], [-1]))