class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     def HasSubtree(self, pRoot1, pRoot2):
#         '''树的子结构'''
#         if pRoot1 == None or pRoot2 == None: return False
#         return self.helper(pRoot1, pRoot2)

#     def helper(self, pRoot1, pRoot2):
#         if pRoot2 == None: return True
#         if pRoot1 == None: return pRoot1 == pRoot2
#         res = False
#         if pRoot1.val == pRoot2.val:
#             res = self.helper(pRoot1.left, pRoot2.left) and self.helper(pRoot1.right, pRoot2.right)
#         return res or self.helper(pRoot1.left, pRoot2) or self.helper(pRoot1.right, pRoot2)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2: return False
        return self.help(pRoot1, pRoot2)
    
    def help(self, pRoot1, pRoot2):
        if not pRoot1: return pRoot1 == pRoot2
        if not pRoot2: return True
        res = False
        if pRoot1.val == pRoot2.val: res = self.help(pRoot1.left, pRoot2.left) and self.help(pRoot1.right, pRoot2.right)
        return res or self.help(pRoot1.left, pRoot2) or self.help(pRoot1.right, pRoot2)