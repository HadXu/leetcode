def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m, n = len(grid), len(grid[0])
    blocks = 0
    neighbours = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                blocks += 1
                if j + 1 < n and grid[i][j + 1] == 1:
                    neighbours += 1
                if i + 1 < m and grid[i + 1][j] == 1:
                    neighbours += 1

    return blocks * 4 - neighbours * 2


if __name__ == '__main__':
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    res = islandPerimeter(grid)
    print(res)