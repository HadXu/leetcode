class Solution:
	def longestValidParentheses(self, s: str) -> int:
		dp = [0] * len(s)
		res = 0
		for i in range(len(s)):
			if s[i] == ')':
				dp[i] = dp[i-2] + 2 if (i-2) >= 0 else 2
				res = max(dp[i], res)
			else:
				if i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
					 





if __name__ == '__main__':
	s = '()(())'
	res = Solution().longestValidParentheses(s)
	print(res)
     