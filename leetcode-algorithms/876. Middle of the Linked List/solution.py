class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def middleNode(head):
	i = j = head
	while i.next and i.next.next:
		i = i.next.next
		j = j.next

	if i.next:
		j = j.next

	return j


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


	e.next = None

	# while a:
	# 	print(a.val)
	# 	a = a.next

	middle = middleNode(a)
	print(middle.val)

