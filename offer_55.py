class ListNode:
    def __init__(self, x, node = None):
        self.val = x
        self.next = node
def print_list_link(pHead):
    while pHead:
        print(pHead.val)
        pHead = pHead.next
    
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead: return pHead

        p1, p2 = None, pHead

        while p2:
            if p2.next and p2.val == p2.next.val:
                value = p2.val
                while p2.next and p2.next.val == value:
                    p2 = p2.next
                if not p1:
                    pHead = p2.next
                else:
                    p1.next = p2.next
            else:
                p1 = p2
            p2 = p2.next

        return pHead

pHead = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2))))))
t = Solution()
print_list_link(t.deleteDuplication(pHead))


