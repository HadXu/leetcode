def networkDelayTime(times, N, K):
	"""
	:type times: List[List[int]]
	:type N: int
	:type K: int
	:rtype: int
	"""
	dist = [65535] * (N+1)

	dist[K] = 0   # 当前节点

	for i in range(0,N):
		for (u,v,w) in times:
			if (dist[u]!= 65535) and (dist[v] > dist[u] + w):
				dist[v] = dist[u] + w

	maxwait = max(dist[1:])

	return -1 if maxwait == 65535 else maxwait






if __name__ == '__main__':
	times = [[2,1,1],[2,3,1],[3,4,1]]
	N = 4
	K = 2

	res = networkDelayTime(times,N,K)
	print(res)



