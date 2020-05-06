from typing import List
class Solution:
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		if not envelopes:
			return 0

		from functools import cmp_to_key
		def cmp(a, b):
			if a[0] == b[0]:
				return b[1] - a[1]
			else:
				return a[0] - b[0]

		tmp = sorted(envelopes, key=cmp_to_key(cmp))

		ll = [x[1] for x in tmp]

		dp = [1] * len(ll)

		for i in range(len(ll)):
			for j in range(i):
				if ll[i] > ll[j]:
					dp[i] = max(dp[i], dp[j]+1)

		return max(dp)


def f(nums):
	res = set()
	track = []
	def fun(nums, track):
		if len(track) == len(nums):
			res.add(tuple(track))
			return

		for i in range(len(nums)):
			if nums[i] in track:
				continue
			track.append(nums[i])
			fun(nums, track)
			del track[-1]

	fun(nums, track)
	return res

x = f([1,2,3])
print(x)

# x = []
# x.append([1,2])
# x.append([1,2])
# x.append([1,2])
# print(x)

if __name__ == '__main__':
	# envelopes = [[5,4],[6,4],[6,7],[2,3]]
	# s = Solution().maxEnvelopes(envelopes)

	# print(s)
	# f([1,2,3])
	# print(res)
	pass