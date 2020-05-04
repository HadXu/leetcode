from typing import List
from itertools import permutations
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		if len(nums) == 1:
			return [nums]

		res = []
		perms = self.permute(nums[1:])
		for each in perms:
			for i in range(len(each)+1):
				p = each[:i]+[nums[0]]+each[i:]
				res.append(p)
		return res







if __name__ == '__main__':
	x = [1,2,3]
	res = Solution().permute(x)
	print(res)