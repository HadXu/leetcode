from typing import List

class Solution:
	def mincostTickets(self, days: List[int], costs: List[int]) -> int:
		travel = set(days)
		dp = [0] * 366
		for i in range(1, 366):
			if i not in travel:
				dp[i] = dp[i-1]
			else:
				dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2]);


		return dp[-1]





if __name__ == '__main__':
	days = [1,4,6,7,8,20]
	costs = [2,7,15]

	res = Solution().mincostTickets(days, costs)

	print(res)