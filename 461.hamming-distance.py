class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        sx, sy = bin(x), bin(y)

        sx, sy = sx[2:], sy[2:]
        lenx, leny = len(sx), len(sy)

        if lenx > leny:
            sx, sy = sy, sx
            lenx, leny = leny, lenx

        # print(lenx, leny)
        sx = '0' * (leny-lenx) + sx

        cnt = 0
        # print(sx, sy)
        for i in range(leny):
            if sx[i] != sy[i]: cnt += 1

        return cnt

#
# s = Solution()
# print s.hammingDistance(3, 1)
#


