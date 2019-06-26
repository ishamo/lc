class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        board = [[ i for i in range(n)] for j in range(n) ]

        x, y = 0, 0
        val = 1

        dxdy = [(1,0), (0,1), (-1,0),(0,-1)]

        while val < n*n:
            board[x][y] = val
            if x + y =

            val += 1
