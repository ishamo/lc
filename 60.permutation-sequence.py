class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import permutations

        pool = list(range(1, n+1))

        j = 0
        g = permutations(pool)
        while j < k:
            element = next(g)
            j += 1

        return ''.join([str(item) for item in element])
#
#
# s = Solution()
# print s.getPermutation(4, 9)
#
