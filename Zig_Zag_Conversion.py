class Solution:
    def convert(self, s: 'str', numRows: 'int')  -> 'str':
        res = ['' for item in range(numRows)]
        if numRows == 1: return s
        
        sign = False
        count = 0
        for item in s:
            res[count] += item
            if count == 0 or count == numRows - 1: sign = not sign
            count += 1 if sign else -1

        return "".join(res)


s = "ffddff"
t = Solution()
print(t.convert(s, 3))