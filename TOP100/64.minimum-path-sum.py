class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        DP = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1:
                    DP[i][j] = DP[i][j-1] + grid[i-1][j-1]
                elif j == 1:
                    DP[i][j] = DP[i-1][j] + grid[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i-1][j-1]

        return DP[m][n]

#
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# s = Solution()
# print s.minPathSum(grid)
#
