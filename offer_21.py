class Solution:
    def IsPopOrder(self, pushV, popV):
        '''栈的压入, 弹出序列'''
        stack = []
        while popV:
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
        