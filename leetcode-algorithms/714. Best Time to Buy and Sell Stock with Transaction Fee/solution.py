class Solution:
	def maxProfit(self, prices, fee: int) -> int:
		if not prices:
			return 0

		dp_0 = 0
		dp_1 = -float('inf')
		for p in prices:
			dp_0 = max(dp_0, dp_1 + p - fee)
			dp_1 = max(dp_1, dp_0 - p)
		return dp_0



if __name__ == '__main__':
	prices = [1, 3, 2, 8, 4, 9]
	fee = 2
	s = Solution().maxProfit(prices, fee)
	print(s)