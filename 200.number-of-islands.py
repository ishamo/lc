class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        visited = [[0] * n] * m # this is WRONG!!!
        visited = [[0 for c in range(n)] for r in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.BFS(i, j, m, n, visited, grid)
        return count


    def BFS(self, i, j, m, n, visited, grid):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1' and not visited[i][j]:
            visited[i][j] = 1
            dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
            for k in range(4):
                self.BFS(i+dx[k], j+dy[k], m, n, visited, grid)
#
#
# if __name__ == '__main__':
#     grid = [['0', '1', '0'],
#             ['1', '0', '1'],
#             ['0', '1', '0']]
#
#     s = Solution()
#     c = s.numIslands(grid)
#     print(c)
