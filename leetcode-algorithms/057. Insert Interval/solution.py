class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	def __str__(self):
		return '[{},{}]'.format(self.start,self.end)
	def __repr__(self):
		return '[{},{}]'.format(self.start,self.end)


def insert(intervals, newInterval):
	"""
	:type intervals: List[Interval]
	:type newInterval: Interval
	:rtype: List[Interval]
	"""

	s,e = newInterval.start,newInterval.end
	left = []
	right = []
	for v in intervals:
		if v.end<s:
			left += v,
		elif v.start > e:
			right += v,
		else:
			s = min(s,v.start)
			e = max(e,v.end)

	return left + [Interval(s,e)] + right



if __name__ == '__main__':
	intervals = [Interval(1,3),Interval(6,9)]
	newInterval = Interval(2,5)
	res = insert(intervals, newInterval)

	print(newInterval,)
	print(res)