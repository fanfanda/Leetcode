class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    count = 0
    def KthNode(self, pRoot, k):
        if not pRoot: return pRoot
        node = self.KthNode(pRoot.left, k)
        if node: return node
        self.count += 1
        if self.count == k: return pRoot
        node = self.KthNode(pRoot.right, k)
        if node: return node
        
    

t = Solution()
pRoot = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
print(t.KthNode(pRoot, 2))
# print(t.res)
