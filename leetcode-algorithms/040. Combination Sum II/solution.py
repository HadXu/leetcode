def combinationSum(candidates, target):
	"""
	:type candidates: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""
	def dfs(nums,target, index, path, res):
		if target<0:
			return
		if target == 0:
			res.append(path)
			return
		for i in range(index, len(nums)):
			if i > index and nums[i] == nums[i-1]:
				continue
			dfs(nums, target-nums[i], i+1, path + [nums[i]], res)

	res = []
	candidates.sort()
	dfs(candidates, target, 0, [], res)

	return res


if __name__ == '__main__':
	candidates = [2,5,2,1,2]
	target = 5
	res = combinationSum(candidates,target)
	print(res)