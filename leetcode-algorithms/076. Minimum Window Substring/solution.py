from collections import defaultdict
def fun(s, T):
	need = defaultdict(int)
	windows = defaultdict(int)
	for c in T:
		need[c] += 1

	left = right = 0
	valid = 0
	res = 100000
	start = 0
	while right < len(s):
		c = s[right]
		right += 1
		if c in need:
			windows[c] += 1
			if windows[c] == need[c]:
				valid += 1

		while valid==len(need):
			if right - left < res:
				start = left
				res = right - left

			d = s[left]
			left += 1
			if d in need:
				if windows[d] == need[d]:
					valid -= 1
				windows[d] -= 1

	if res == 100000:
		return ''
	else:
		return s[start:start + res]


if __name__ == '__main__':
	s = 'EBBANCF'
	T = 'ABC'

	res = fun(s, T)
	print(res)


