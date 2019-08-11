class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    '''二叉树的深度'''
    def TreeDepth(self, pRoot):
        if not pRoot: return 0
        right = self.TreeDepth(pRoot.right) + 1
        left = self.TreeDepth(pRoot.left) + 1
        return max(right, left)




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot: return 0
        result = self.helper(pRoot, 0)
        return result
    def helper(self, pRoot, count):
        if not pRoot: return count
        maxs = max(self.helper(pRoot.left, count), self.helper(pRoot.right, count)) + 1
        return maxs
        