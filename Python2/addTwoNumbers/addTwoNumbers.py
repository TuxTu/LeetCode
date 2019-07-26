# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        tempNode = root
        carry = 0
        while l1 or l2:
    	    v1 = 0
    	    v2 = 0
    	    if l1:
    		    v1 = l1.val
    		    l1 = l1.next
    	    if l2:
    		    v2 = l2.val
    		    l2 = l2.next
    	    newNode = ListNode((v1 + v2 + carry) % 10)
    	    tempNode.next = newNode
    	    tempNode = newNode
    	    carry = (v1 + v2 + carry) / 10
        if carry != 0:
    	    newNode = ListNode(carry)
    	    tempNode.next = newNode
        if root.next:
    	    return root.next
        else:
    	    return None
