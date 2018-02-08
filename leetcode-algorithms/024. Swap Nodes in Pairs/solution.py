class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def swapPairs(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""

	dummy = ListNode(None)
	dummy.next = head
	curr = dummy

	while curr.next and curr.next.next:
		first = curr.next
		second = curr.next.next
		first.next = second.next
		curr.next = second
		curr.next.next = first
		curr = curr.next.next
	return dummy.next