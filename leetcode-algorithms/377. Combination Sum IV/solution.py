
def combinationSum4(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	res = [0 for _ in range(target+1)]
	res[0] = 1

	for i in range(1,len(res)):
		for j in range(len(nums)):
			if i-nums[j]>=0:
				res[i] += res[i-nums[j]]
	
	return res[target]








if __name__ == '__main__':
	nums = [3,2,1]
	target = 4

	res = combinationSum4(nums,target)

	print(res)

