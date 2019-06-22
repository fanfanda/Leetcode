class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode: return pNode
        if pNode.right:
            pNode = pNode.right
            while(pNode.left):
                pNode = pNode.left
            return pNode
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None