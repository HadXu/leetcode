def canFinish(numCourses, prerequisites):
	"""
	:type numCourses: int
	:type prerequisites: List[List[int]]
	:rtype: bool
	"""
	graph = [[] for _ in range(numCourses)]
	visit = [0 for _ in range(numCourses)]

	for x,y in prerequisites:
		graph[x].append(y)



	def dfs(i):
		if visit[i] == -1:
			return False
		if visit[i] == 1:
			return True
		visit[i] = -1
		for j in graph[i]:
			if not dfs(j):
				return False
		visit[i] = 1
		return True


	for i in range(numCourses):
		if not dfs(i):
			return False

	return True



if __name__ == '__main__':
	numCourses = 3
	prerequisites = [[1,0],[0,1]]

	res = canFinish(numCourses, prerequisites)
	print(res)



