class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if not board or not board[0]: return False

        m, n = len(borad), len(board[0])

        def BFS(i, j):
            dxdy = [(1,0),(-1,0),(0,1),(0,-1)]

            # TODO


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if BFS(i, j): return True

        return False

