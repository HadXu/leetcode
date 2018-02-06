def generateParenthesis(n):
	"""
	:type n: int
	:rtype: List[str]
	"""
	def DFS(left, right, out, res):
		if left > right:
			return
		if left==0 and right == 0:
			res.append(out)
		else:
			if left>0:
				DFS(left-1,right,out+'(',res)
			if right>0:
				DFS(left,right-1,out+')',res)

	res = []
	DFS(n,n,"",res)
	return res





if __name__ == '__main__':
	n = 3
	res = generateParenthesis(n)
	print(res)