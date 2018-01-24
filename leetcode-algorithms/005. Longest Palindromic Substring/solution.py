class Solution:
	maxLen = 0
	lo = 0
	def longestPalindrome(self, s):
		if len(s)<2:
			return s
		for i in range(len(s)):
			self.f(s,i,i)
			self.f(s,i,i+1)
		return s[Solution.lo:Solution.lo+Solution.maxLen]

	def f(self,s,j,k):
		while j>=0 and k<len(s) and s[j]==s[k]:
			j -= 1
			k += 1
		if Solution.maxLen < k-j-1:
			Solution.lo = j+1
			Solution.maxLen = k-j-1


if __name__ == '__main__':
	s = 'cbbd'
	so = Solution()

	res = so.longestPalindrome(s)
	print(res)