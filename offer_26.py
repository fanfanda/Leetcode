class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
    
# class Solution:
#     def Convert(self, pRootOfTree):
#         if not pRootOfTree: return pRootOfTree
#         result = []
#         self.helper(pRootOfTree, result)
#         for i in range(len(result) - 1):
#             result[i].right = result[i + 1]
#             result[i + 1].left = result[i]
            
#         return result[0]

#     def helper(self, pRootOfTree, result):
#         if not pRootOfTree: return 
#         self.helper(pRootOfTree.left, result)
#         result.append(pRootOfTree)
#         self.helper(pRootOfTree.right, result)



class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree: return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right: return pRootOfTree
        pLeft = self.Convert(pRootOfTree.left)
        if pLeft:
            temp = pLeft
            while temp.right:
                temp = temp.right
            pRootOfTree.left = temp
            temp.right = pRootOfTree

        pRight = self.Convert(pRootOfTree.right)
        if pRight:
            pRootOfTree.right = pRight
            pRight.left = pRootOfTree

        return pLeft if pLeft else pRootOfTree 

test = TreeNode(7, TreeNode(4, TreeNode(3), TreeNode(5)), TreeNode(10, TreeNode(9), TreeNode(12)))
t = Solution()
# print(t.Convert(test))
s = t.Convert(test)
while s:
    print(s.val)
    s = s.right