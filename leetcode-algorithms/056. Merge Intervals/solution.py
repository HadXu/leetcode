class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	def __str__(self):
		return '[{},{}]'.format(s,end)
	def __repr__(self):
		return '[{},{}]'.format(self.start,self.end)

def merge(intervals):
	"""
	:type intervals: List[Interval]
	:rtype: List[Interval]
	"""
	if len(intervals)<1:
		return intervals
	intervals = sorted(intervals,key=lambda x:x.start)

	res = []

	start = intervals[0].start
	end = intervals[0].end

	for v in intervals:
		if v.start <= end:
			end = max(end, v.end)
		else:
			res.append(Interval(start,end))
			start = v.start
			end = v.end
	res.append(Interval(start,end))
	return res

if __name__ == '__main__':
	A = Interval(1,3)
	B = Interval(2,6)
	C = Interval(8,10)
	D = Interval(16,18)
	intervals = [A,C,D,B]

	res = merge(intervals)

	print(res)

