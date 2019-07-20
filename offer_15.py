class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# class Solution:
#     def ReverseList(self, pHead):
#         '''链表翻转'''
#         pre = None
#         while pHead:
#             cur = pHead.next
#             pHead.next = pre
#             pre = pHead
#             pHead = cur
#         return pre

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None
        while pHead:
            temp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = temp
        return pre