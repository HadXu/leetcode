class Solution:
	def simplifyPath(self, path: str) -> str:
		path = path.split('/')

		stack = []

		print(path)

		for item in path:
			if item == '..':
				if stack:
					stack.pop()
			elif item and item != '.':
				stack.append(item)

		return '/' + '/'.join(stack)






if __name__ == '__main__':
	path = '/a/./b/../../c/'

	res = Solution().simplifyPath(path)

	print(res)