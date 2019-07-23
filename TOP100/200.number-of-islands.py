class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def DFS(grid, r, c):
            row, col = len(grid), len(grid[0])
            if not 0 <= r < row or not 0 <= c < col: return
            if not grid[r][c] == '1': return
            grid[r][c] = '0'

            dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
            for dx, dy in dxdy:
                if 0 <= r+dx < row and 0 <= c+dy < col and grid[r+dx][c+dy] == '1':
                    DFS(grid, r+dx, c+dy)


        if not grid or not len(grid[0]): return 0

        row, col = len(grid), len(grid[0])

        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    DFS(grid, r, c)

        return count
# 
# 
# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# print Solution().numIslands(grid)
