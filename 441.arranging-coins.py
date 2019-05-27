class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        i = 1
        level = 0
        while total+i <= n:
            total += i
            i += 1
            level += 1

        return level
