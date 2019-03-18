# def reverse(strr):
#     if not strr: return
#     reverse(strr[1:])
#     print(strr[0], end = '')

# class Solution:
#     def reverseString(self, s: 'List[str]') -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         def helper(start, end, strr):
#             if start >= end:
#                 return
#             strr[start], strr[end] = strr[end], strr[start]
#             return helper(start + 1, end - 1, strr)
#         return helper(0, len(s) - 1, s)

# t = Solution()
# test = ['h', 'e', 'l', 'l', 'o']
# t.reverseString(test)
# print(test)

# class Solution:
#     def generate(self, numRows: int) -> 'List[List[int]]':
#         memo = {}
#         def helper(i, j):
#             if (i, j) not in memo:
#                 if i == j or j == 0:
#                     memo[i, j] = 1
#                     return memo[i, j]
#                 memo[i, j] = helper(i - 1, j - 1) + helper(i - 1, j)
#                 return memo[i, j]
#             return memo[i, j]
#         res = []
#         for i in range(numRows):
#             temp = []
#             for j in range(i + 1):
#                 temp.append(helper(i, j))
#             res.append(temp)
#         return res

# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         row = [1]
#         for _ in range(rowIndex):
#             row = [x + y for x, y in zip([0]+row, row+[0])]
#         return row

# t = Solution()
# print(t.getRow(5))

class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        def helper(num):
            if num not in memo:
                if num <= 1:
                    memo[num] = num
                    return memo[num]
                memo[num] = helper(num - 1) + helper(num - 2)
                return memo[num]
            return memo[num]
        return helper(N)

t = Solution()
print(t.fib(5))