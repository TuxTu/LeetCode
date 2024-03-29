# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#52ms,13.7MB
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head
        
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    temp.next = l1
                    temp = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    temp = l2
                    l2 = l2.next
            elif l1 == None:
                temp.next = l2
                break
            elif l2 == None:
                temp.next = l1
                break
        
        return head.next
