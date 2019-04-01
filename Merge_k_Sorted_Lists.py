from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        head = cur = ListNode(0)
        queue = PriorityQueue()
        for item in lists:
            if item: queue.put((item.val, item))
        while queue.empty():
            val, node = queue.get()
            cur.next = node
            cur = cur.next
            if node.next: queue.put(node.next.val, node.next)
            
        return head.next

t = Solution()

