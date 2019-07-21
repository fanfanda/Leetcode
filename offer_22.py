class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     '''顺序打印二叉树, bfs广度优先遍历, 用队列'''
#     def PrintFromTopToBottom(self, root):
#         queue, res = [], []
#         if not root: return res
#         queue.append(root); res.append(root.val)
#         while queue:
#             temp = queue.pop(0)
#             if temp.left:
#                 queue.append(temp.left); res.append(temp.left.val)
#             if temp.right:
#                 queue.append(temp.right); res.append(temp.right.val)
#         return res



class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root: return []
        queue, res = [root, ], []
        while queue:
            temp = queue.pop(0)
            res.append(temp.val)
            if temp.left: queue.append(temp.left)
            if temp.right: queue.append(temp.right)
        return res

t = Solution()
print(t.PrintFromTopToBottom(TreeNode(4)))