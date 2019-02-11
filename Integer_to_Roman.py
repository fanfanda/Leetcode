class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = str(num)
        _len = len(num)
        res = ""
        while _len:
            temp_num = int(num[0])
            if temp_num == 4: 
                res += roman_list[_len * 2 - 2] + roman_list[_len * 2 - 1]
            elif temp_num == 9:
                res += roman_list[_len * 2 - 2] + roman_list[_len * 2]
            elif temp_num >= 5:
                res += roman_list[_len * 2 - 1] + roman_list[_len * 2 - 2] * (temp_num - 5)
            else:
                res += roman_list[_len * 2 - 2] * temp_num
            num = num[1:]
            _len -= 1
        return res

t = Solution()
print(t.intToRoman(123))
