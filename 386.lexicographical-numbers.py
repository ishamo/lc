class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        pool = list(range(1, n+1))
        pool.sort(key=lambda x: str(x))
        return pool
#
#
# s = Solution()
# print s.lexicalOrder(13)
#
