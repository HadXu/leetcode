def searchInsert(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	return len([x for x in nums if x<target])

if __name__ == '__main__':
	nums = [1,3,5,6]
	target = 7

	res = searchInsert(nums, target)

	print(res)