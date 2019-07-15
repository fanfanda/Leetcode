# class Solution:
#     def replaceSpace(self, s):
#         # 替换空格
#         temp = s.split(' ')
#         return '%20'.join(temp)

# t = Solution()
# print(t.replaceSpace("123 342"))

class Solution(object):
    def __init__(self):
        # board 存储一种解法（作为缓存）
        self.board = []
        # boards 存储所有解法（作为结果）
        self.boards = []
    def solve_n_queens(self, n):
        """
        :param n: int:
        :return: self.boards: list[list[int]]
        """
        self.board = [0 for i in range(n)]
        self.solve_line(0, n)
        return self.boards
    # 解决前 row 列
    def solve_line(self, row, n):
        if row == n:
            self.boards.append([i for i in self.board])
            return
        else:
            for col in range(n):
                if self.is_valid(row, col):
                    self.board[row] = col
                    self.solve_line(row + 1, n)
                    self.board[row] = 0
    # 监测 (row,col) 是否与 0~row-1 行发生冲突
    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col:
                return False
            if i + self.board[i] == row + col:
                return False
            if i - self.board[i] == row - col:
                return False
        return True