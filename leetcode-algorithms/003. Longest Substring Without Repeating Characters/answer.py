class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        v_i = {}
        j = 0
        res = 0
        for i,v in enumerate(s):
        	if v in v_i:
        		j = max(j,v_i[v]+1)
        	v_i[v] = i
        	res = max(res,i-j+1)
        return res




if __name__ == '__main__':
	s = Solution()
	ss = 'abcababcdefg'
	res = s.lengthOfLongestSubstring(ss)
	print(res)