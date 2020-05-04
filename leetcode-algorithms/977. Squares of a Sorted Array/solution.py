from typing import List
class Solution:
	def sortedSquares(self, A: List[int]) -> List[int]:
		j = 0
		N = len(A)
		while j<N and A[j] < 0:
			j += 1
		i = j - 1

		ans = []
		while 0 <= i and j < N:
			print(i, j)
			if A[i]**2 < A[j]**2:
				ans.append(A[i]**2)
				i -= 1
			else:
				ans.append(A[j]**2)
				j += 1

		while i >= 0:
			ans.append(A[i]**2)
			i -= 1
		while j <N:
			ans.append(A[j]**2)
			j += 1
		return ans


if __name__ == '__main__':
	A = [-4,-1,0,3,10]
	res = Solution().sortedSquares(A)
	print(res)
