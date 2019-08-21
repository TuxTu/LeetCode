# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        tmp = ListNode(0)
        tmp.next = head.next
        head.next = self.swapPairs(tmp.next.next)
        tmp.next.next = head

        return tmp.next