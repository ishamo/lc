class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        strx = bin(x)[2:]
        stry = bin(y)[2:]
        strx = (32 - len(strx)) * '0' + strx
        stry = (32 - len(stry)) * '0' + stry
        count = 0
        for i in range(32):
            if not strx[i] == stry[i]:
                count += 1
        return count
