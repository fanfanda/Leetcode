class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 反向输出链表的值
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]

t = Solution()
print(t.printListFromTailToHead(ListNode(5)))