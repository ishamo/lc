class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        astr = bin(n)
        for idx, c in enumerate(astr[1:], 1):
            if astr[idx] == astr[idx-1]: return False

        return True
