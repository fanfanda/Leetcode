# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            head_next = head.next
            head.next = pre
            pre = head
            head = head_next
        return pre
        
        

head = ListNode(4, next = ListNode(3, None))
t = Solution()
t.reverseList(ListNode(3))
        