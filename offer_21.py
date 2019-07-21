# class Solution:
#     def IsPopOrder(self, pushV, popV):
#         '''栈的压入, 弹出序列'''
#         stack = []
#         while popV:
#             if stack and stack[-1] == popV[0]:
#                 stack.pop()
#                 popV.pop(0)
#             elif pushV:
#                 stack.append(pushV.pop(0))
#             else:
#                 return False
#         return True
        
class Solution:
    def IsPopOrder(self, pushV, popV):
        temp = []
        while pushV:
            if popV[0] == pushV[0]: popV.pop(0)
            else: temp.append(pushV[0])
            pushV.pop(0)
        return temp[::-1] == popV

t = Solution()
print(t.IsPopOrder([1, 2, 3, 4, 5], [2, 4, 5, 3, 1]))