class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy_node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            x1 = 0 if not l1 else l1.val
            x2 = 0 if not l2 else l2.val
            sums = x1 + x2 + carry
            temp_val = sums % 10
            carry = sums // 10
            cur.next = ListNode(temp_val)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy_node.next
        