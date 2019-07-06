# def queen(A, cur = 0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur + 1)
# queen([None] * 5)

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:07:18 2018

@author: Saul
"""

class Solution:
    def judge(self, threshold, i, j):
        if sum(map(int,str(i) + str(j))) <= threshold:
            return True
        else:
            return False

    def findgrid(self, threshold, rows, cols, matrix, i, j):
        count = 0
        if i < rows and j < cols and i >= 0 and j >= 0 and self.judge(threshold,i,j) and matrix[i][j] == 0:
            matrix[i][j] = 1
            count = 1 + self.findgrid(threshold, rows, cols, matrix, i, j + 1) \
            + self.findgrid(threshold, rows, cols, matrix, i, j - 1) \
            + self.findgrid(threshold, rows, cols, matrix, i + 1, j) \
            + self.findgrid(threshold, rows, cols, matrix, i - 1, j)
        return count

    def movingCount(self, threshold, rows, cols):
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        count = self.findgrid(threshold, rows, cols, matrix, 0, 0)
        print(matrix)
        return count