class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def sortList(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""

	from heapq import heappush,heappop
	res  = []
	if not head:
		return head
	while head:
		heappush(res,head.val)
		head = head.next

	p = ListNode(heappop(res))
	q = p
	for _ in range(len(res)):
		temp = ListNode(heappop(res))
		q.next = temp
		q = temp


	return p


if __name__ == '__main__':
	A = ListNode(-1)
	B = ListNode(5)
	C = ListNode(3)
	D = ListNode(4)
	E = ListNode(0)

	A.next = B
	B.next = C
	C.next = D
	D.next = E

	p = A

	p = sortList(p)

	while p:
		print(p.val)
		p = p.next



        