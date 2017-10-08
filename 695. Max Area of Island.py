def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    col = len(grid[0])

    def dfs(r, c, g):
        if not (0 <= r < row and 0 <= c < col and g[r][c]):
            return 0
        g[r][c] = 0
        return 1 + sum([dfs(r + x[0], c + x[1], g) for x in [(0, 1), (0, -1), (1, 0), (-1, 0)]])

    return max([dfs(r, c, grid) for r in range(row) for c in range(col)])


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    res = maxAreaOfIsland(grid)
    print(res)
