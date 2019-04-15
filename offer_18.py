class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Mirror(self, root):
        '''二叉树的镜像'''
        if root == None: return 
        root.left, root.right = root.right, root.left
        self.Mirror(root.right)
        self.Mirror(root.left)
        return root

