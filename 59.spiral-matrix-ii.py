class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        board = [[ 0 for i in range(n)] for j in range(n)]

        x, y = 0, 0
        dx, dy = 0, 1
        for i in range(1, n*n+1):
            board[x][y] = i
            if board[(x+dx)%n][(y+dy)%n]:
                dx, dy = dy, -dx

            x += dx
            y += dy

        return board
