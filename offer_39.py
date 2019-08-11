class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot: return 0
        right = self.TreeDepth(pRoot.right) + 1
        left = self.TreeDepth(pRoot.left) + 1
        return max(right, left)
    def IsBalanced_Solution(self, pRoot):
        '''二叉树是否平衡'''
        if not pRoot: return True
        if abs(self.TreeDepth(pRoot.right) - self.TreeDepth(pRoot.left)) < 2: return True
        else: return False

