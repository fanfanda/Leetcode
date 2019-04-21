class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    '''二叉树查找某一路径和'''
    def FindPath(self, root, expectNumber):
        res, path = [], []
        def helper(root, target, sums):
            path.append(root.val)
            sums += root.val
            if root.left:
                helper(root.left, target, sums)
            if root.right:
                helper(root.right, target, sums)
            if not root.left and not root.right:
                if sums == target:
                    res.append(path[:])
            path.pop()
            return 
        if root:
            helper(root, expectNumber, 0)
        return res
    
tree = TreeNode(10, TreeNode(15),  TreeNode(17))
t = Solution()
print(t.FindPath(tree, 25))