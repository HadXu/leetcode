# 最长等待时间

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
* N will be in the range [1, 100].
* K will be in the range [1, N].
* The length of times will be in the range [1, 6000].
* All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

## 使用迪杰斯科拉算法

```python
dist = [65535] * (N+1)

dist[K] = 0   # 当前节点

for i in range(0,N):
    for (u,v,w) in times:
        if (dist[u]!= 65535) and (dist[v] > dist[u] + w):
            dist[v] = dist[u] + w

maxwait = max(dist[1:])
return -1 if maxwait == 65535 else maxwait
```