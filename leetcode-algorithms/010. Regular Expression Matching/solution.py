import re

def isMatch(s, p):
	"""
	:type s: str
	:type p: str
	:rtype: bool
	"""
	if s == None or p == None:
		return False


	dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
	dp[0][0] = True

	for i in range(1,len(p)+1):
		if p[i-1] == '*':
			dp[0][i] = dp[0][i-2]

	print(dp)

	for i in range(1,len(s)+1):
		for j in range(1,len(p)+1):
			if (p[j-1] == '.') or (p[j-1] == s[i-1]):
				dp[i][j] = dp[i-1][j-1]
			else:
				if 	p[j-1] == '*':
					if (p[j-2] == s[i-1]) or (p[j-2] == '.'):
						dp[i][j] = dp[i][j-2] or dp[i-1][j]
					else:
						dp[i][j] = dp[i][j-2]

	return dp[len(s)][len(p)]


if __name__ == '__main__':
	s = 'abcdd'
	p = 'a*b'
	print(isMatch(s,p))

