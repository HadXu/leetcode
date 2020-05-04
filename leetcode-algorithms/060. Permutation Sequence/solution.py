from itertools import permutations
class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		p = permutations(range(1, n+1))

		res =  map(str, list(list(p)[k-1]))

		return ''.join(res)


if __name__ == '__main__':
	n = 4
	k = 9

	res = Solution().getPermutation(n,k)
	print(res)

        