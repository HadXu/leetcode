def removeElement(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""

	begin = 0
	for i in range(len(nums)):
		if nums[i] != val:
			nums[begin] = nums[i]
			begin += 1
	return begin



        

if __name__ == '__main__':
	nums = [3,2,2,3]
	val = 3
	res = removeElement(nums, val)
	print(res)