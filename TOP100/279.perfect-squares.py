import math
class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        DP = [5 for i in range(n+1)]
        DP[0], DP[1] = 0, 1
        for i in range(2, n+1):
            for j in range(0, i):
                q = int(math.sqrt(i-j))
                if j + q*q == i:
                    DP[i] = min(DP[i], DP[j]+1)

        return DP[n]


s = Solution()
print s.numSquares(71)
