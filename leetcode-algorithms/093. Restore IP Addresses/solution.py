class Solution:
	def restoreIpAddresses(self, s: str):
		
		def helper(ip):
			if not ip or (ip[0] == '0' and len(ip) > 1) or int(ip) > 255:
				return False
			return True

		res = []
		n = len(s)

		for i in range(3):
			for j in range(i+1, i+4):
				for k in range(j+1, j+4):
					if i<n and j<n and k < n:
						temp1 = s[:i+1]
						temp2 = s[i+1:j+1]
						temp3 = s[j+1:k+1]
						temp4 = s[k+1:]

						if all(map(helper, [temp1,temp2,temp3,temp4])):
							res.append(temp1 + "." + temp2 + "." + temp3 + "." + temp4)


		return res



if __name__ == '__main__':
	s = '25525511135'
	res = Solution().restoreIpAddresses(s)
	print(res)