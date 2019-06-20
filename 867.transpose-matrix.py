class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]: return []

        m, n = len(A), len(A[0])

        ret = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            for j in range(n):
                ret[j][i] = A[i][j]

        return ret
