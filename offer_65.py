class Solution:
    def hasPath(self, matrix, rows, cols, path):
        '''矩阵中的路径'''
        res_matrix = [] 
        for i in range(rows):
            res_matrix.append(list(matrix[:cols]))
            matrix = matrix[cols:]
        
        for i in range(rows):
            for j in range(cols):
                assist_matrix = [[False for t in range(cols)] for k in range(rows)]
                if self.isValid(res_matrix, i, j, path, assist_matrix, rows, cols):
                    return True
        return False
    def isValid(self, matrix, i, j, path, assist_matrix, rows, cols):
        if not path: return True
        if i < 0 or i >= rows or j < 0  or j >= cols or assist_matrix[i][j] or (path[0] != matrix[i][j]): return False
        else:
            assist_matrix[i][j] = True # 每个不同的递归掉用并不共享assist_matrix
            return self.isValid(matrix, i + 1, j, path[1:], assist_matrix, rows, cols) or self.isValid(matrix, i - 1, j, path[1:], assist_matrix, rows, cols) or self.isValid(matrix, i, j + 1, path[1:], assist_matrix, rows, cols) or self.isValid(matrix, i, j - 1, path[1:], assist_matrix, rows, cols)
        return False

t = Solution()
print(t.hasPath('ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEHJIGQEM'))