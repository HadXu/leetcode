from typing import List
class Solution:
	def divisorGame(self, N: int) -> bool:
		dp = [False] * (N+1)
		
		for i in range(2, N+1):
			for j in range(1, i):
				if i % j == 0:
					if dp[i-j] == False:
						dp[i] = True
						break

		return dp[N]

if __name__ == '__main__':
	N = 2
	res = Solution().divisorGame(N)
	print(res)



