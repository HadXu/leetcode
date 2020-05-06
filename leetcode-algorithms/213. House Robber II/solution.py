
class Solution:
	def rob(self, nums) -> int:
		if not nums:
			return 0
		if len(nums)==1:
			return nums[0]

		if len(nums)==2:
			return max(nums[0], nums[1])

		def fun(nums):
			N = len(nums)
			dp = [0] * N

			dp[0] = nums[0]
			dp[1] = max(nums[0], nums[1])

			for i in range(2, N):
				dp[i] = max(dp[i-1], dp[i-2] + nums[i])

			return max(dp)

		res1 = fun(nums[:-1])
		res2 = fun(nums[1:])
		return max(res1, res2)


if __name__ == '__main__':
	nums = [2,3,4,5]

	s = Solution().rob(nums)

	print(s)