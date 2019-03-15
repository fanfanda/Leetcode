# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
def print_tree(node):
    if node == None:
        return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)

class Solution:
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)
        view = []
        collect(root, 0)
        return view

test = TreeNode(1, TreeNode(2, right = TreeNode(5)), TreeNode(3, right = TreeNode(4)))
print_tree(test)
t = Solution()
print(t.rightSideView(test))