def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	
	lo = 0
	hi = len(nums)
	while lo < hi:
		mid = (hi+lo) // 2
		num = 0
		if (nums[mid]<nums[0]) == (target < nums[0]):
			num = nums[mid]
		else:
			if target < nums[0]:
				num = -float('inf')
			else:
				num = float('inf')

		if target > num:
			lo = mid + 1
		elif target < num:
			hi = mid
		else:
			return mid
	return -1



if __name__ == '__main__':
	nums = [4,5,6,7,0,1,2]
	res = search(nums,1)
	print(res)
