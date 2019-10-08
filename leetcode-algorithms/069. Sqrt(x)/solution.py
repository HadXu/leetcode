class Solution:
	def mySqrt(self, x: int) -> int:
		
		if x == 0:
			return 0


		cur = 8.
		while True:
			pre = cur
			cur = (cur + x / cur) / 2
			if abs(cur**2 - x) < 0.00001:
				return int(cur)





if __name__ == '__main__':
	x = 8

	res = Solution().mySqrt(x)

	print(res)