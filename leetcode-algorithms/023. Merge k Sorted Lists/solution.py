class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def mergeKLists(lists):
	"""
	:type lists: List[ListNode]
	:rtype: ListNode
	"""

	from queue import PriorityQueue
	dummy = ListNode(None)
	curr = dummy
	q = PriorityQueue()

	for node in lists:
		if node:
			q.put((node.val, node))

	while q.qsize()>0:
		curr.next = q.get()[1]
		curr = curr.next
		if curr.next:
			q.put((curr.next.val,curr.next))
	return dummy.next



if __name__ == '__main__':
	a = ListNode(1)
	b = ListNode(3)
	a.next = b
	c = ListNode(5)
	b.next = c


	d = ListNode(0)
	e = ListNode(4)
	d.next = e

	lists = [a,d]


	res = mergeKLists(lists)

	while res:
		print(res.val)
		res = res.next









