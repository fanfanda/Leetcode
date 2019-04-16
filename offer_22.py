class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    '''顺序打印二叉树, bfs广度优先遍历, 用队列'''
    def PrintFromTopToBottom(self, root):
        queue, res = [], []
        if not root: return res
        queue.append(root); res.append(root.val)
        while queue:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left); res.append(temp.left.val)
            if temp.right:
                queue.append(temp.right); res.append(temp.right.val)
        return res

t = Solution()
print(t.PrintFromTopToBottom(TreeNode(4)))