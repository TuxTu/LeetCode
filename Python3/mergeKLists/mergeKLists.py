# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#out of time
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        temp = ans
        while True:
            notNone = 0
            curMin = 9999
            i = 0
            minIndex = 0
            for list in lists:
                if list != None:
                    notNone += 1
                else:
                    i += 1
                    continue
                if list.val < curMin:
                    curMin = list.val
                    minIndex = i
                i += 1
            if notNone == 0:
                break
            temp.next = lists[minIndex]
            temp = temp.next
            print(minIndex)
            lists[minIndex] = lists[minIndex].next

        return ans.next

#132ms,18MB
class Solution2:
	def mergeKLists(self, lists: List[ListNode]) -> List[ListNode]:
		s = []
		for list in lists:
			while list != None:
				s.append(list.val)
				list = list.next

		s.sort()
		head = ListNode(0)
		temp = head
		for num in s:
			node = ListNode(num)
			temp.next = node
			temp = temp.next

		return head

from queue import PriorityQueue

#72ms,20.9MB
class Solution3:
	def mergeKLists(self, lists: List[ListNode]) -> List[ListNode]:
		q = PriorityQueue()
		for l in lists:
			if l:
				q.put((l.val, l))

		head = temp = ListNode(0)

		while not q.empty():
			val, node = q.get()
			temp.next = ListNode(val)
			temp = temp.next
			node = node.next
			if node:
				q.put((node.val, node))

		return head.next

aNumb = a = ListNode(0)
'''a.next = ListNode(4)
a = a.next
a.next = ListNode(5)
'''

bNumb = b = ListNode(0)
b.next = ListNode(3)
b = b.next
b.next = ListNode(4)

print(Solution3().mergeKLists([aNumb, bNumb]))
