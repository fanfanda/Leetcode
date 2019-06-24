class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.isSymmetricalTree(pRoot.left, pRoot.right)
    def isSymmetricalTree(self, TLeft, TRight):
        if not TLeft and not TRight:
            return True
        if not TLeft or not TRight:
            return False
        if TLeft.val == TRight.val:
            return self.isSymmetricalTree(TLeft.left, TRight.right) and self.isSymmetricalTree(TLeft.right, TRight.left)
        return False