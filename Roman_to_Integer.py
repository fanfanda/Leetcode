class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        res = 0
        while s:
            try:
                if roman_dict[s[0]] < roman_dict[s[1]]:
                    res += roman_dict[s[1]] - roman_dict[s[0]]
                    s = s[2:]
                else:
                    res += roman_dict[s[0]]
                    s = s[1:]
            except IndexError:
                res += roman_dict[s[0]]
                s = s[1:]
        return res

t = Solution()
print(t.romanToInt('III'))