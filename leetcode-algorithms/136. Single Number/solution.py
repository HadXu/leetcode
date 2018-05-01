
def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	res = 0
	for i in nums:
		res ^= i
	return res



if __name__ == '__main__':
	nums = [4,1,2,1,2]
	print(singleNumber(nums))