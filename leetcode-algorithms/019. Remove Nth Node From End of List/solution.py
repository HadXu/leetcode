class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def removeNthFromEnd(head, n):
	"""
	:type head: ListNode
	:type n: int
	:rtype: ListNode
	"""

	fast = slow = head
	for _ in range(n):
		fast = fast.next
	if not fast:
		return head.next
	while fast.next:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return head




if __name__ == '__main__':
	a = ListNode(1)
	b = ListNode(2)
	a.next = b
	c = ListNode(3)
	b.next = c
	d = ListNode(4)
	c.next = d
	e = ListNode(5)
	d.next = e

	head = removeNthFromEnd(a,2)

	while head:
		print(head.val)
		head = head.next



