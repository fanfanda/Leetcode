# class RandomListNode:
#     def __init__(self, x, next = None, random = None):
#         self.label = x
#         self.next = next
#         self.random = random
# class Solution:
#     '''复杂链表的复制'''
#     def clone_node(self, pHead):
#         cur = pHead
#         while cur:
#             clone_node = RandomListNode(cur.label)
#             clone_node.next = cur.next
#             cur.next = clone_node
#             cur = clone_node.next
        
#     def reset_random(self, pHead):
#         cur = pHead
#         while cur:
#             clone_node = cur.next
#             if cur.random:
#                 clone_node.random = cur.random.next
#             cur = clone_node.next
        
#     def split_link(self, pHead):
#         cloNode = pHead
#         pHead = pHead.next
#         while cloNode.next:
#             node = cloNode.next
#             cloNode.next = node.next
#             cloNode = node
#         return pHead

#     def Clone(self, pHead):
#         if not pHead: return pHead
#         self.clone_node(pHead)
#         self.reset_random(pHead)
#         return self.split_link(pHead)

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self, pHead):
        

n = RandomListNode(3, RandomListNode(4), RandomListNode(5))
t = Solution()
t.Clone(n)