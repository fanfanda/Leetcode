class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 根据先序/中序构造二叉树
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0: return
        root = TreeNode(pre[0])
        for index in range(len(tin)):
            if tin[index] == root.val:
                break
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index + 1])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root