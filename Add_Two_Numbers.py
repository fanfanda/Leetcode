# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        temp_head = dummy_head
        sign = 0

        while (l1 and l2):
            result = (l1.val + l2.val + sign) % 10
            sign = 1 if (l1.val + l2.val + sign) > 9 else 0

            temp_head.next = ListNode(result)

            l1 = l1.next
            l2 = l2.next
            temp_head = temp_head.next

        while (l1):
            result = (l1.val + sign) % 10
            sign = 1 if (l1.val + sign) > 9 else 0

            temp_head.next = ListNode(result)

            l1 = l1.next
            temp_head = temp_head.next

        while (l2):
            result = (l2.val + sign) % 10
            sign = 1 if (l2.val + sign) > 9 else 0

            temp_head.next = ListNode(result)

            l2 = l2.next
            temp_head = temp_head.next
        
        if sign:
            temp_head.next = ListNode(sign)
            
        return dummy_head.next

def generate_list(mylist = [1, 2, 3, 4]):
    head = ListNode(mylist[0])
    temp = head

    for item in mylist[1:]:
        temp.next = ListNode(item)
        temp = temp.next
    
    return head

def print_list(head):
    while head:
        if head.next:
            print(head.val, end = '->')
        else:
            print(head.val)
        head = head.next
         

l1 = generate_list([2, 4, 3])
l2 = generate_list([5, 6, 4])

t = Solution()
result_head = t.addTwoNumbers(l1, l2)
print_list(result_head)