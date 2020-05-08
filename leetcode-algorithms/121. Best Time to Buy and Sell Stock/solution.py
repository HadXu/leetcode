class Solution:
	def maxProfit(self, prices) -> int:
		dp_0 = 0
		dp_1 = -float('inf')

		for p in prices:
			dp_0 = max(dp_0, dp_1 + p)
			dp_1 = max(dp_1, -p)
		return dp_0



if __name__ == '__main__':
	prices = [7,1]
	s = Solution().maxProfit(prices)

	print(s)