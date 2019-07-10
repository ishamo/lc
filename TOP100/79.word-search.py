# coding: utf-8
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not word: return True
        if not board or not board[0]: return False

        root = {}
        node = root
        for w in word:
            node.setdefault(w, {})
            node = node[w]
        node['#'] = True

        m, n = len(board), len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]

        result = []

        def DFS(board, i, j, node, visited, result):
            if '#' in node:
                result.append(1)
                return
            m, n = len(board), len(board[0])
            if not 0 <= i < m or not 0 <= j < n: return
            if visited[i][j]: return
            if board[i][j] not in node: return

            visited[i][j] = 1
            DFS(board,i+1,j,node[board[i][j]],visited,result)
            DFS(board,i-1,j,node[board[i][j]],visited,result)
            DFS(board,i,j+1,node[board[i][j]],visited,result)
            DFS(board,i,j-1,node[board[i][j]],visited,result)
            visited[i][j] = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    node = root
                    DFS(board, i, j, node, visited, result)
                    if result: return True

        return False


#
#
# board = [
#   ['A', 'B', 'C', 'E'],
#   ['S', 'F', 'E', 'S'],
#   ['A', 'D', 'E', 'E']
# ]
#
#
# s = Solution()
# word = 'ABE'
# # word = 'ABCCED'
# # word = 'SED'
# print s.exist(board, word)
#
#
# ✘ Wrong Answer
# ✘ 83/87 cases passed (N/A)
# ✘ testcase: '[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]\n"ABCESEEEFS"'
# ✘ answer: false
# ✘ expected_answer: true
