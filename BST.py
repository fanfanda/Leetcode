class Node():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class Binary_Search_Tree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        y = None
        x = self.root

        while x:
            y = x
            if node.val < x.val: x = x.left
            else: x = x.right
        node.parent = y
        if not y: self.root = node
        elif node.val < y.val: y.left = node
        else: y.right = node

def print_BST(node):
    if node:
        print_BST(node.left)
        print(node.val, end = ' ')
        print_BST(node.right)

def tree_minimum(node):
    while node.left:
        node = node.left
    return node

def tree_maximum(node):
    while node.right:
        node = node.right
    return node

def tree_search(node, k):
    if not node or k == node.val: return node
    if k < node.val: return tree_search(node.left, k)
    else: return tree_search(node.right, k)

def transplant(T, u, v):
    if not u.parent: T.root = v
    elif u == u.parent.left: u.parent.left = v
    else: u.parent.right = v
    if v: v.parent = u.parent

def tree_delete(T, node):
    if not node.left: return transplant(T, node, node.right)
    elif not node.right: return transplant(T, node, node.left)
    else: 
        y = tree_minimum(node.right)
        if y.parent != node:
            transplant(T, y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(T, node, y)
        y.left = node.left
        y.left.parent = y

t = Binary_Search_Tree()
t.insert(3); t.insert(-1); t.insert(2); t.insert(2); t.insert(18)

print_BST(t.root)
