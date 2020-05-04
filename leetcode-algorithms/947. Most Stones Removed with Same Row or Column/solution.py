from typing import List
class DSU:
    def __init__(self, M):
        self.p = list(range(M))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.p[x] = y

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})

if __name__ == '__main__':
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    res = Solution().removeStones(stones)
    print(res)
