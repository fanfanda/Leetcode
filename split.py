def split(strr, sign):
    res = []
    def helper(strr, cur):
        if not strr:
            if cur: res.append(cur) 
            return res
        if strr[0] == sign:
            if cur: res.append(cur)
            helper(strr[1:], '')
        else:
            helper(strr[1:], cur + strr[0])
    helper(strr, '')
    return res

print(split('/ffd/asd/fdea/', '/'))