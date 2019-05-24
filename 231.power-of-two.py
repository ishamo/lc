class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n & n-1: return False

        while n > 1:
            n = n >> 1

        return True if n == 1 else False
