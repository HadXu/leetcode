class Solution:
    def maxProfit(self, prices) -> int:
        dp_i10, dp_i20 = 0 ,0
        dp_i11, dp_i21 = -float('inf'), -float('inf')
        for p in prices:
            dp_i20 = max(dp_i20, dp_i21 + p)
            dp_i21 = max(dp_i21, dp_i10 - p)

            dp_i10 = max(dp_i10, dp_i11 + p)
            dp_i11 = max(dp_i11, -p);  # 第一次买
        return dp_i20





if __name__ == '__main__':
	prices = []
	s = Solution().maxProfit(prices)

	print(s)