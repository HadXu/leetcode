from typing import List
class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]

		N = len(nums)
		dp = [0] * N

		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])

		for i in range(2, N):
			dp[i] = max(dp[i-1], dp[i-2] + nums[i])


		return max(dp)




if __name__ == '__main__':
	nums = [0]
	res = Solution().rob(nums)
	print(res)