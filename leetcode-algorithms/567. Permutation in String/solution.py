class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		if len(s1) > len(s2):
			return False

		s1map = [0] * 26
		s2map = [0] * 26

		for i in range(len(s1)):
			s1map[ord(s1[i])-97] += 1
			s2map[ord(s2[i])-97] += 1

		for i in range(len(s2)-len(s1)):
			if s1map == s2map:
				return True

			s2map[ord(s2[i+len(s1)]) - 97] += 1
			s2map[ord(s2[i]) - 97] -= 1

		if s1map == s2map:
			return True

		return False





if __name__ == '__main__':
	s1 = 'ab'
	s2 = 'eidbaooo'
	s = Solution()
	print(s.checkInclusion(s1, s2))