class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def FindKthToTail(self, head, k):
#         '''链表中倒数第k个节点'''
#         p1 = p2 = head
#         for i in range(k):
#             if p2 == None: return None
#             p2 = p2.next
#         while p2:
#             p2 = p2.next
#             p1 = p1.next
#         return p1

class Solution:
    def FindKthToTail(self, head, k):
        pre = back = head
        for i in range(k):
            if back: back = back.next
            else: return back
        while back:
            pre = pre.next
            back = back.next
        return pre

t = Solution()
head = cur = ListNode(1)
ss = [2, 3, 4, 5]
for item in ss:
    cur.next = ListNode(item)
    cur = cur.next
print(t.FindKthToTail(head, 3))