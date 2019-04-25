class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        '''两个链表的第一个公共结点'''
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        common = None
        while stack1 and stack2:
            temp = stack1.pop()
            if temp == stack2.pop():
                common = temp
        return common