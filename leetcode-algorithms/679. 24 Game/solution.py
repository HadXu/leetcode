from typing import List
from operator import truediv, mul, add, sub

class Solution:
	def judgePoint24(self, nums: List[int]) -> bool:
		if not nums: return False
		if len(nums) == 1: return abs(nums[0] - 24) < 1e-8
		for i in range(len(nums)):
			for j in range(len(nums)):
				if i != j:
					B = [nums[k] for k in range(len(nums)) if i != k != j]
					for op in (truediv, mul, add, sub):
						if (op is add or op is mul) and j > i: continue
						if op is not truediv or nums[j]:
							B.append(op(nums[i], nums[j]))
							if self.judgePoint24(B): return True
							B.pop()

		return False

if __name__ == '__main__':
	nums = [4, 1, 8, 7]
	res = Solution().judgePoint24(nums)
	print(res)



     	
