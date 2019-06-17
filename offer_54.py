class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        pFast = pSlow = pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next

            if pFast == pSlow:
                pFast = pHead

                while pFast != pSlow:
                    pFast = pFast.next
                    pSlow = pSlow.next
                return pFast
        return None