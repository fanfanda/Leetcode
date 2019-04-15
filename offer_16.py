class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        '''合并两个有序链表'''
        dummy = cur = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 or pHead2

        return dummy.next