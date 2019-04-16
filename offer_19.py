class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        left, right, top, bot = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bot:
            for i in range(left, right + 1):
                # print('->', matrix[top][i])
                res.append(matrix[top][i])
            if top < bot:
                for i in range(top + 1, bot + 1):
                    # print('|', matrix[i][right])
                    res.append(matrix[i][right])
            if left < right and top < bot:
                for i in range(right - 1, left - 1, -1):
                    # print('<-', matrix[bot][i])
                    res.append(matrix[bot][i])
            if top < bot and left < right:
                for i in range(bot - 1, top, -1):
                    # print('|', matrix[i][left])
                    res.append(matrix[i][left]) 
            left += 1; right -= 1; top += 1; bot -= 1
        return res

t = Solution()
print(t.printMatrix([[1],[2],[3],[4],[5]]))