class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return board
        m, n = len(board), len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]

        def BFS(i, j):
            print('i,j', i, j)
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and board[i][j] in ['O', '*']:
                visited[i][j] = 1
                board[i][j] = '*'
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                for k in range(4):
                    BFS(i+dx[k], j+dy[k])

        for i in range(m):
            for j in [0, -1]:
                if board[i][j] == 'O': board[i][j] = '*'

        for j in range(n):
            for i in [0, -1]:
                if board[i][j] == 'O': board[i][j] = '*'

        for i in range(m):
            for j in range(n):
                if board[i][j] == '*' and not visited[i][j]:
                    BFS(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
#
#
# if __name__ == '__main__':
#     board = [
#         ['X', 'X', 'X', 'X'],
#         ['X', 'O', 'O', 'X'],
#         ['X', 'X', 'O', 'X'],
#         ['X', 'O', 'O', 'X']
#     ]
#     board = [
#         ["X","O","X","O","X","O"],
#         ["O","X","O","X","O","X"],
#         ["X","O","X","O","X","O"],
#         ["O","X","O","X","O","X"]]
#     s = Solution()
#     s.solve(board)
#     print(board)
