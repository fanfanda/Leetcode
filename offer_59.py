class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
# class Solution:
#     def Print(self, pRoot):
#         result, stack1, stack2 = [], [pRoot], []
#         if not pRoot:
#             return result
#         while stack1 or stack2:
#             temp_list = []
#             while stack1:
#                 temp = stack1.pop()
#                 temp_list.append(temp.val)
#                 if temp.left:
#                     stack2.append(temp.left)
#                 if temp.right:
#                     stack2.append(temp.right)
#             if temp_list:
#                 result.append(temp_list)
#             temp_list = []
#             while stack2:
#                 temp = stack2.pop()
#                 temp_list.append(temp.val)
                
#                 if temp.right:
#                     stack1.append(temp.right)
#                 if temp.left:
#                     stack1.append(temp.left)
#             if temp_list:
#                 result.append(temp_list)
#         return result
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        nodeStack = [pRoot]
        result = []
        while nodeStack:
            res = []
            nextStack = []
            for i in nodeStack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            result.append(res)
            nodeStack = nextStack
        return result

root = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))

t = Solution()
print(t.Print(root))