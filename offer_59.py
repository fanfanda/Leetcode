class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def Print(self, pRoot):
        result, stack1, stack2 = [], [pRoot], []
        if not pRoot:
            return result
        while stack1 or stack2:
            temp_list = []
            while stack1:
                temp = stack1.pop(0)
                temp_list.append(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            if temp_list:
                result.append(temp_list)
            temp_list = []
            while stack2:
                temp = stack2.pop(0)
                temp_list.append(temp.val)
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)
            if temp_list:
                result.append(temp_list)
        return result
        
root = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))

t = Solution()
print(t.Print(root))