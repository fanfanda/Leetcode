class Solution:
    def Find(self, target, array):
        '''有没有更简单的做法'''
        m, n = len(array), len(array[0])
        row, col = 0, n - 1
        while col >= 0 and row < m:
            if target == array[row][col]: return True
            elif target < array[row][col]: col -= 1
            else: row += 1
        return False

t = Solution()
print(t.Find(2, [[0, 1, 2], [1, 2, 3]]))