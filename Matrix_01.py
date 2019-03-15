import collections
class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        r, c = len(matrix), len(matrix[0])
        q = collections.deque()
        visted = set()

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visted.add((i, j))

        while q:
            i, j = q.popleft()
            for m, n in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= m < r and 0 <= n and n < c and (m, n) not in visted:
                    matrix[m][n] = matrix[i][j] + 1
                    q.append((m, n))
                    visted.add((m, n))
        return matrix

test = [[0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]]

t = Solution()
s = t.updateMatrix(test)