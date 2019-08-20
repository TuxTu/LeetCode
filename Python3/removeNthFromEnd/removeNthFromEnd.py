#52ms,13.6MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeLength = 0
        temp = head
        while temp != None:
            nodeLength += 1
            temp = temp.next
        
        targetPoint = nodeLength - n
        lazyHead = ListNode(0)
        lazyHead.next = head
        temp = lazyHead
        
        for i in range(targetPoint):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return lazyHead.next
