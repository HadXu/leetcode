def validateStackSequences(pushed, popped):
	"""
	:type pushed: List[int]
	:type popped: List[int]
	:rtype: bool
	"""
	temp = []
	i = 0
	for p in pushed:
		temp.append(p)
		while len(temp)>0 and temp[-1] == popped[i]:
			temp.pop()
			i += 1
	return len(temp) == 0

if __name__ == '__main__':
	pushed = [1,2,3,4,5]
	popped = [4,5,3,2,1]

	res = validateStackSequences(pushed,popped)

	print(res)
			