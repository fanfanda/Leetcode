class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        res = []
        if n == 0: return []
        def helper(left, right, current):
            if right > left: return
            if left == n and right == n: 
                res.append(current)
                return
            if left < n:
                helper(left + 1, right, current + '(')
            if right < n:
                helper(left, right + 1, current + ')')

        helper(0, 0, '')
        return res

t = Solution()
print(t.generateParenthesis(3))