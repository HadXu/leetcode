import collections
def groupAnagrams(strs):
	"""
	:type strs: List[str]
	:rtype: List[List[str]]
	"""
	groups = collections.defaultdict(list)
	for s in strs:
		groups[tuple(sorted(s))].append(s)
	return list(map(sorted, groups.values()))






if __name__ == '__main__':
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	res = groupAnagrams(strs)
	print(res)