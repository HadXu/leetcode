class Solution:
	def maxProfit(self, prices) -> int:
		if not prices:
			return 0
		dp_0 = 0
		dp_1 = -float('inf')

		res = 0

		for p in prices:
			tmp = dp_0
			dp_0 = max(dp_0, dp_1 + p)
			dp_1 = max(dp_1, tmp - p)
		return dp_0






if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	s = Solution().maxProfit(prices)

	print(s)