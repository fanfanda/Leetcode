class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def ReverseList(self, pHead):
        '''链表翻转'''
        pre = None
        while pHead:
            cur = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = cur
        return pre