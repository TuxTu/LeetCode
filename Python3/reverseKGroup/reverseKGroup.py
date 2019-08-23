# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#80ms,15.2MB
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        numbH = tmp = ListNode(0)
        tmp.next = head

        tmpL = []
        for i in range(k):
            if head != None:
                tmpL.append(head.val)
                head = head.next
            else:
                return numbH.next

        for i in range(k - 1, -1, -1):
            tmp.next = ListNode(tmpL[i])
            tmp = tmp.next

        if head != None:
            tmp.next = self.reverseKGroup(head, k)

        return numbH.next