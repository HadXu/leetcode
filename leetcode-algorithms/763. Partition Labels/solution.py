from typing import List


class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		d = {c:i for i,c in enumerate(S)}

		j = anchor = 0
		res = []

		for i, c in enumerate(S):
			j = max(j, d[c])
			if i == j:
				res.append(i - anchor + 1)
				anchor = i+1

		return res


if __name__ == '__main__':
	s = 'ababcbacadefegdehijhklij'
	res = Solution().partitionLabels(s)
	print(res)