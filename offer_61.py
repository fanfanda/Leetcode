class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # 返回对应节点TreeNode
    count = 0
    def KthNode(self, pRoot, k):
        res = []
        def helper(pRoot, k):
            if not pRoot:
                return pRoot
            helper(pRoot.left, k)
            res.append(pRoot)
            self.count += 1
            if self.count == k:
                return
            helper(pRoot.right, k)
        helper(pRoot, k)
        return res[k - 1] if 0 < k <= len(res) else None
        
        # if not pRoot:
        #     return pRoot
        # print(len(self.res), k)
        # if len(self.res) == k:
        #     return self.res[-1]
        # self.KthNode(pRoot.left, k)
        # self.res.append(pRoot.val)
        # self.KthNode(pRoot.right, k)

t = Solution()
pRoot = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
print(t.KthNode(pRoot, 1))
# class Solution:
#     def recursion(self, count, pRoot):
#         if count == 0 or not pRoot:
#             return pRoot
#         else:
#             self.recursion(count, pRoot.left)
#             self.recursion(count - 2, pRoot.right)
#     # 返回对应节点TreeNode
#     def KthNode(self, pRoot, k):
#         return self.recursion(k - 1, pRoot)