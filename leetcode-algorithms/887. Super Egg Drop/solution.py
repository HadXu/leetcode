class Solution:
	def superEggDrop(self, K: int, N: int) -> int:
		cache = {}

		def dp(k,n):
			if k==1: return n
			if n==0: return 0

			if (k,n) in cache:
				return cache[(k,n)]

			# res = float('inf')
			# for x in range(1, n+1):
			# 	res = min(max(dp(k-1, x-1),dp(k, n-x))+1,res)

			res = float('inf')
			lo, hi = 1, n
			while lo <= hi:
				mid = (lo+hi) // 2

				broken = dp(k - 1, mid - 1)
				not_broken = dp(k, n - mid)

				if broken > not_broken:
					hi = mid - 1
					res = min(res, broken + 1)
				else:
					lo = mid + 1
					res = min(res, not_broken + 1)

			cache[(k,n)] = res
			return res

		return dp(K, N)



if __name__ == '__main__':
	K = 6
	N = 5000

	res = Solution().superEggDrop(K, N)

	print(res)


