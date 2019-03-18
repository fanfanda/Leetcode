class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        temp_dict = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def helper(current, next):
            if not next:
                res.append(current)
            else:
                for i in temp_dict[next[0]]:
                    helper(current + i, next[1:])
        res = []
        if digits:
            helper('', digits)
        return res

t = Solution()
ss = t.letterCombinations('532')
# print(t.letterCombinations('5'))