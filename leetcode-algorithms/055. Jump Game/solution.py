def canJump(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	reach = 0
	for i,v in enumerate(nums):
		if reach < i+1:
			break
		reach = max(reach, i+1+v)

	return reach>=len(nums)






if __name__ == '__main__':
	nums = [2,3,1,1,4]
	res = canJump(nums)
	print(res)