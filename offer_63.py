class Solution:
    def maxInWindows(self, num, size):
        if size >= len(num):
            return max(num)
        result = []
        temp = max(num[:size])
        result.append(temp)

        for i in range(1, len(num) - size):
            result.append(max())
