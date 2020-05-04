from typing import List
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		res = 0
		nums = set(nums)
		for x in nums:
			if x - 1 not in nums:
				y = x + 1
				while y in nums:
					y += 1
				res = max(res, y-x)

		return res





if __name__ == '__main__':
	nums = [100, 4, 200, 1, 3, 2]
	res = Solution().longestConsecutive(nums)
	print(res)