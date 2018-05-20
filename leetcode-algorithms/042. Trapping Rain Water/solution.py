def trap(height):
	"""
	:type height: List[int]
	:rtype: int
	"""

	res = 0
	maxleft = 0
	maxright = 0

	left = 0
	right = len(height) - 1

	while left < right:
		if height[left]<=height[right]:
			if height[left]>=maxleft:
				maxleft = height[left]
			else:
				res += maxleft - height[left]
			left += 1
		else:
			if height[right]>maxright:
				maxright = height[right]
			else:
				res += maxright - height[right]
			right -= 1
	return res



if __name__ == '__main__':
	height = [0,1,0,8]

	res = trap(height)
  
	print(res)