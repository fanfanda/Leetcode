class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.seri = ""
        self.s = []

    def Serialize(self, root):
        if not root:
            return 'n'
        return str(root.val) +',' + self.Serialize(root.left) +','+ self.Serialize(root.right)

    # 定义清楚递归函数实现的功能，把字符串，反序列化为二叉树
    def Deserialize(self, s):
        if len(s) == 0:
            return      
        if self.s == []:
            self.s = s.split(',')   
        v = self.s.pop(0) # 左子树pop完成之后，轮到右子树对应的序列
        if v != 'n':
            root = TreeNode(int(v))           
            root.left = self.Deserialize(self.s)
            root.right = self.Deserialize(self.s)
            return root
        else:
            return None

root = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
t = Solution()
print(t.Serialize(root))