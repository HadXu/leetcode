import queue
def levelOrder(root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	res = []
	p = root
	q = queue()
	q.put(p)
	while not q.empty():
		for t in q.get():
			if t.left:
				q.put(t.left)
			if t.right:
				q.put(t.right)
			temp.append(t.val)
		res.append(temp)
	return res